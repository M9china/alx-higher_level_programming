#!/bin/bash
size=$(curl -s -w %{size_download} $1 -o /dev/null)
echo "$size"