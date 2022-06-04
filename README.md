# Remove / disable bloatware from Samsung Galaxy devices

Use this project to remove / disable bloatware from your Samsung Galaxy device.

## Dependencies

- Python 3
- ADB: ADB must be present and the ADB home directory must be provided as `ADB_HOME` environment variable. Configuration via `.env` file is supported
- Mobile device must be connected and accessible by ADB, i.e. running `adb devices` must show your device

## Usage

The file `app-list.json` contains the configuration for all apps that should be removed / disabled. Modify it as you need.

Then, run the following command to remove / disable the bloatware:

```bash
galaxy-cleanup.sh
```

> Use the `-s` flag to provide your mobile's serial in case you have several devices connected at the same time, e.g. `galaxy-cleanup.sh -s 123456`
>
> Use the `-v` switch to increase verbosity, e.g. `galaxy-cleanup.sh -v`

The command above writes to stdout, stderr and to the `out.log` log file.

## Other links

- [https://www.youtube.com/watch?v=HtPCCZPqanI](https://www.youtube.com/watch?v=HtPCCZPqanI)
- [https://krispitech.com/how-to-remove-bloatware-from-samsung-galaxy-s22-ultra/](https://krispitech.com/how-to-remove-bloatware-from-samsung-galaxy-s22-ultra/)
- [https://www.alliancex.org/shield/apps.html](https://www.alliancex.org/shield/apps.html)
- [https://forum.xda-developers.com/t/how-to-debloat-adb-the-ultimate-adb-debloating-thread-for-the-s20-u-series.4089089/](https://forum.xda-developers.com/t/how-to-debloat-adb-the-ultimate-adb-debloating-thread-for-the-s20-u-series.4089089/)
- [https://github.com/khlam/debloat-samsung-android/issues/33](https://github.com/khlam/debloat-samsung-android/issues/33)
