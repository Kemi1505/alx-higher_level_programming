#!/bin/bash
# Takes a URL , sends a request and display its byte siz
curl -s "$1" | wc -c
