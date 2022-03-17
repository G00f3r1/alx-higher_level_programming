#!/usr/bin/bash
# script that sends a JSON POST request to a URL passed as the first argument, and displays the body
curl -sXHd POST "content-type: application/json" @"$2" "$1"
