#!/bin/bash
# script that that causes the server to respond with a message containing You got me!, in the body of the response
curl -sL -X PUT -H "Origin: CatchMeee" -d "user_id=98" 0.0.0.0:5000/catch_me
