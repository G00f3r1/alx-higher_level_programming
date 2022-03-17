#!/usr/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -sLHdX "Origin: " "user_id=98" PUT 0.0.0.0:5000/catch_me
