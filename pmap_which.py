#!/usr/bin/python2
# Author: Guiroux Hugo <gx.hugo@gmail.com / http://hugoguiroux.blogspot.fr/>
# See LICENSE

import csv
import sys
import svgwrite
from PIL import Image, ImageDraw

# Check param
if len(sys.argv) < 2:
    print "Usage: %s addr"%sys.argv[0]
    exit(0)

addr = int(sys.argv[1], 16)

# Read csv file from stdin
info = csv.reader(sys.stdin)
for row in info:
    start = int(row[0], 16)
    stop = int(row[1], 16)

    if addr >= start and addr <= stop:
        print "%s belongs to \t\t%s (%s) : %s -> %s"%(sys.argv[1], row[3], row[2], row[0], row[1])
        exit(0)
print "%s not mapped"%sys.argv[1]
