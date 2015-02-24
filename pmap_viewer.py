#!/usr/bin/python2

import csv
import sys
import svgwrite
from PIL import Image, ImageDraw

# Check param
if len(sys.argv) < 2:
    print "Usage: %s output_file"%sys.argv[0]
    exit(0)

# Read csv file from stdin
info = csv.reader(sys.stdin)
data = []
for row in info:
    data.append({'start': row[0], 'stop': row[1], 'rights': row[2], 'name': row[3]})

# Take minimum size as unitary
min_size = min([int(d['stop'], 16) - int(d['start'], 16) + 1 for d in data])

# Compute min/max for main rectangle
cur_addr = 0
size = 0
is_64 = False
for d in data:
    start = int(d['start'], 16)
    stop = int(d['stop'], 16)

    # For whole in @ space, add one unitary space
    if cur_addr != start:
        size += 1

    size += (stop - start + 1) / min_size
    cur_addr = stop + 1

    if len("%x"%start) > 8:
        is_64 = True

size = int(size)

# Config margin
top_bottom_margin = 10
left_margin = 10
right_margin_for_text = 100
memory_width = 100
text_left_margin = 10
text_max_size = 100
scale = 100.0

img = Image.new("RGB", (right_margin_for_text + memory_width + text_max_size, int(size/scale) + 1 + top_bottom_margin * 2), "white")
dwg = ImageDraw.Draw(img)

# Draw main rectangle
dwg.rectangle(
    [(left_margin, top_bottom_margin),
     (right_margin_for_text + memory_width, int(size/scale) + 1 + top_bottom_margin)],
    outline='black')

# Print @ right
size = 0
cur_addr = 0
for d in data:
    start = int(d['start'], 16)
    stop = int(d['stop'], 16)
    s_addr = "0x%0.16x"%cur_addr if is_64 else "0x%0.8x"%cur_addr

    print "Draw %s (%d,%f)"%(s_addr, right_margin_for_text + memory_width + text_left_margin, top_bottom_margin + size/scale)

    # For whole in @ space, print one space
    if cur_addr != start:
        dwg.text((right_margin_for_text + memory_width + text_left_margin, top_bottom_margin + size/scale), s_addr, fill='black')
        size += 1

    size += (stop - start + 1) / min_size
    cur_addr = stop + 1

# Ouput
img.save(sys.argv[1], "PNG")
