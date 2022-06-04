#!/usr/bin/env bash

if [ -f .env ]
then
    export "$(grep -v '^#' .env | xargs)"
fi

python3 ./galaxy-cleanup.py "$@" 2>&1 | tee out.log