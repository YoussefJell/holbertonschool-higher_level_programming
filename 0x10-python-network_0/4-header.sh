#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
