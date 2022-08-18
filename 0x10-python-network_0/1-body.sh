#!/bin/bash
# displays the size of the body of the response if the http_code is 200 OK
arg=$1; if [ $(curl -s -L -w '%{http_code}' "$arg" -o /dev/null) -eq 200 ]; then curl -sL "$arg"; fi
