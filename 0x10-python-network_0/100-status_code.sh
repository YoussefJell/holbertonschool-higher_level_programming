#!/bin/bash
# displays status code
curl -s -L -w '%{http_code}' "$arg" -o /dev/null
