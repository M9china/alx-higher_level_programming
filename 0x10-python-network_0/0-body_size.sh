#!/bin/bash

# Retrieve the content length of a web page
curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '