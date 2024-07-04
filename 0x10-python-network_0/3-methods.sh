#!/bin/bash
#display all the methods that the server will allow
curl -sI "$1" |grep "Allow" | cut -d " " -f 2- 
