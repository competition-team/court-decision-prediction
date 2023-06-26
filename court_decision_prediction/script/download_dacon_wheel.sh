#!/bin/bash

wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1TYnY2KBU9NuR973pB2oqfFCw2dHgpKX7' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1TYnY2KBU9NuR973pB2oqfFCw2dHgpKX7" -O dacon_submit_api-0.0.4-py3-none-any.zip && rm -rf /tmp/cookies.txt
unzip dacon_submit_api-0.0.4-py3-none-any.zip dacon_submit_api-0.0.4-py3-none-any.whl
rm dacon_submit_api-0.0.4-py3-none-any.zip