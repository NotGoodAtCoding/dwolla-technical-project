#!/usr/bin/env bash

cd server
python -m main &
sleep 1
serverpid="$!"
cd ..

dtp-cli

kill "$serverpid"