#!/bin/sh
for dper in `cat src/dper.txt`;do
python3 src/bawangcan.py ${dper} #>>1.log;
done
