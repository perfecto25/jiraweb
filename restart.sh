#!/bin/sh
set -x
app='jiraweb'

lastpid=$(ps -ef | grep ${app}.py | grep -v grep | awk -F" " {'print $2'} | xargs kill -9)

python $app.py &