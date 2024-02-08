#!/bin/bash
# sends a request to URL and displays the size of the response body
curl -s -w %{size_download} $1 -o /dev/null