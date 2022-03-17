#!/bin/bash
# script that sends a JSON POST request to a URL passed as the first argument, and displays the body
curl -sX POST -H "content-type: application/json" -d @"$2" "$1"
