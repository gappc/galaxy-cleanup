import argparse
import json
import os

adb_home = os.getenv("ADB_HOME")

if adb_home == None:
    print("ADB_HOME environment variable missing")
    exit(1)

adb = adb_home + "/adb"


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--serial", help="use device with given serial", type=str)
    parser.add_argument("-v", "--verbose", help="show verbose output", action="store_true")
    args = parser.parse_args()
    return (args.serial, args.verbose)


def read_app_list():
    with open("app-list.json", "r") as read_file:
        return json.load(read_file)


def build_base_cmd(serial):
    return adb if serial == None else adb + " -s " + serial


def build_app_delete_cmd(base_cmd, package):
    return base_cmd + "  shell pm uninstall --user 0 " + package


def build_app_disable_cmd(base_cmd, package):
    return base_cmd + "  shell pm disable-user --user 0 " + package


def build_app_info(app_entry):
    return app_entry["app"] + " (" + app_entry["package"] + ") - " + app_entry["description"]


def main():
    (serial, verbose) = parse_arguments()

    base_cmd = build_base_cmd(serial)

    if verbose:
        print("Base command: " + base_cmd)

    apps = read_app_list()

    for entry in apps:
        package = entry["package"]
        operation = entry["operation"]

        cmd = None

        print("-------------------------------------------")
        if operation == "nop":
            print("DO NOTHING - " + build_app_info(entry))
        elif operation == "delete":
            print("DELETE - " + build_app_info(entry))
            cmd = build_app_delete_cmd(base_cmd, package)
        elif operation == "disable":
            print("DISABLE - " + build_app_info(entry))
            cmd = build_app_disable_cmd(base_cmd, package)
        else:
            print("UNKNOWN - " + build_app_info(entry))

        if cmd != None:
            if verbose:
                print(cmd)
            os.system(cmd)


if __name__ == "__main__":
    main()
