#!/bin/bash
#get the status code
curl -sO /dev/null -w "%{http_code}" "$1"
