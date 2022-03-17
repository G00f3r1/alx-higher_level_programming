#!/usr/bin/bash
# script that sends a request to that URL, and displays the size of the body
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2 
