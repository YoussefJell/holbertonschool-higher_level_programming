#!/bin/bash
# displays status code
echo $(curl -s -L -w '%{http_code}' "$arg" -o /dev/null)
