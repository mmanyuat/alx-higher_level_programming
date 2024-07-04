#!/bin/bash
#check the url provide
curl -s "$1" | wc -c
