#!/bin/sh
rm -f 1.log
for dper in `cat src/dper.txt`;do
python3 src/bawangcan.py ${dper} #>>1.log;
python3 src/bawangcan01.py ${dper} #>>1.log;
done
