#!/usr/bin/env bash
# displays the size of the body of the response if the http_code is 200 OK
arg=$1
STATUS=$(curl -s -L -w '%{http_code}' "$arg" -o /dev/null)
if [ "$STATUS" -eq 200 ]; then
        curl -sL "$arg"
fi
