#!/usr/bin/env bash

cd server
python -m main &
sleep 1
serverpid="$!"
cd ..

pact-verifier --provider-base-url=http://localhost:5001 --pact-url=./pacts/consumer-provider.json

kill "$serverpid"
