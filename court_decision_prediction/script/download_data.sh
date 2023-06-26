#!/bin/bash

wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1yqN-1xYQoMWZimJhxdopX6woT2KomeZh' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1yqN-1xYQoMWZimJhxdopX6woT2KomeZh" -O open.zip && rm -rf /tmp/cookies.txt
mkdir data
unzip open.zip -d data/open
rm open.zip