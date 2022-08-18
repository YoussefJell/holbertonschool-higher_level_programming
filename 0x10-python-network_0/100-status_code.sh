#!/bin/bash
# displays status code
curl -s -L -w '%{http_code}' "$1" -o /dev/null
