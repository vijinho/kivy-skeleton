#!/bin/bash
find . -type f -name "*.pyc" -exec rm {} \;
if [ -z "$1" ];
   then kivy main.py --size='480x800'
else
   kivy main.py --size=$1;
fi
