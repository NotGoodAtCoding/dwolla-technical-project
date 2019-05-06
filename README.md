# Dwolla Technical Project

[![Build Status](https://travis-ci.org/NotGoodAtCoding/dwolla-technical-project.svg?branch=master)](https://travis-ci.org/NotGoodAtCoding/dwolla-technical-project)
[![codecov](https://codecov.io/gh/NotGoodAtCoding/dwolla-technical-project/branch/master/graph/badge.svg)](https://codecov.io/gh/NotGoodAtCoding/dwolla-technical-project)

For this project, I have created a time server and simple client.
The time server has a single endpoint, the root, and returns a response in the format:
``` 
{"currentTime": "05-06-19 18:11:20"}
```

The time is given in the format `MONTH-DAY-YEAR(2) HOUR(24):MINUTE:SECOND` in UTC

## Setup

This project includes some demo and convenience scripts, namely `local_run.sh` and `run_pact.sh` which you may have to 
add permissions to if you wish to use them. 

``` 
# POSIX
chmod +x local_run.sh
chmod +x run_pact.sh
```

### Requirements

``` 
Python 3.6
docker
docker-compose
POSIX machine (not guaranteed to run on Windows)
```

## Server

The server is written in Python 3.6 compliant code and can be started by running:
``` 
# Docker Compose - runs server and client
make up

# Make target to run the server and client for demo purposes
make run 

# directly with python
cd server && python -m main
```


## Client

You can run the client in standalone mode by installing this package:
``` 
make package
```
Then running the executable:
 `dtp-cli`
 
 
Alternatively, you can run the client as a python script with `cd client && python main.py` 


## Testing
Tests can be run with `make test` which will run both unit and contract tests. 

The contract tests use the [pact-python](https://github.com/pact-foundation/pact-python) library and 
verify static interactions between the client and server. 

Due to the nature of the server, the specification for the interaction is very loose, 
only verifying the general format of the response. 