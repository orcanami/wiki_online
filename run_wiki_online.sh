#!/bin/bash
touch test.txt
echo "This is a test!" > test.txt
cd ~/Dropbox/Orcanami/wiki_online/
source ob_venv/bin/activate
cd onlinebot
python onlinebot.py -site:wikipedia:en \
        -page:User:Orcanami/Status -text:"away" -showdiff:False
