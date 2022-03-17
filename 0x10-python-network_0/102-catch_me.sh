#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -sLH "Origin:You got me!" -X PUT 0.0.0.0:5000/catch_me
