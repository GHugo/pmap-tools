#!/usr/bin/python2
# Author: Guiroux Hugo <gx.hugo@gmail.com / http://hugoguiroux.blogspot.fr/>
# See LICENSE

import sys
import subprocess

# Check argument & help
if len(sys.argv) < 2:
    print "pmap_parser returns the process mapping of pid in csv of format:"
    print "from_addr,to_addr,rights,name"
    print
    print "Usage: %s pid"%sys.argv[0]
    exit(0)

# Get the pid
pid = int(sys.argv[1])

# Launch pmap -x pid
proc = subprocess.Popen(['pmap', str(pid)], stdout = subprocess.PIPE)

# Parse every line and print with format :
# from_addr,to_addr,rights,name
first = True
while True:
    line = proc.stdout.readline()
    if line == '':
        break

    if line == "\n":
        continue

    # Cmd line
    if first:
        first = False
        continue

    # Format: address size rights name
    l = line.rstrip().split()
    try:
        addr, size, rights, name = l[0], l[1], l[2], " ".join(l[3:])
        addr = int(addr, 16)
        size = int(size[:-1]) * 1024
        rights = rights[:-1] # last one is for Solaris format respect

        print "%x,%x,%s,%s"%(addr, addr + size - 1, rights, name)
    except IndexError:
        continue
