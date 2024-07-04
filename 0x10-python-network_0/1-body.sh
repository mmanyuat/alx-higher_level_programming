#!/bin/bash
#check the provided url
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1

fi 
URL=$1
response=$(curl -s -w "%{http_code}" "$URL")
body=${response%???}
status_code=${response: -3}

if [ "$status_code" -eq 200 ]; then
	echo "$body"
else
	echo "Response status code is not 200: $status_code"
fi 
