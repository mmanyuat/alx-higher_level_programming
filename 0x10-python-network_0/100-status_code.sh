#!/bin/bash
#get the status code
curl -so /dev/null -w "%{http_code}" "$1"
