pmap-tools
==========

Tools manipulating process virtual memory mapping.

Guiroux Hugo (gx.hugo@gmail.com / http://hugoguiroux.blogspot.fr/)

## pmap_parser:

Retrieve the virtual memory mapping given a pid and output in CSV
format. Platform specific (only Linux for now, using `pmap`).

Format: `from_addr,to_addr,rights,name`
Usage: `pmap_parser.py pid`

## pmap_which:

Given a csv file of process mapping on stdin and a memory address, gives at
which memory region the address belongs.

Usage: `pmap_which.py addr`

# Examples:

For chromium, find which memory regions contains 0x7f7b44438001:
```
pmap_parser.py $(pidof -s chromium) | pmap_which.py 0x7f7b44438001
```

Results:
```
0x7f7b44438001 belongs to            libfontconfig.so.1.8.0 (r-x-) : 7f7b44438000 -> 7f7b44636fff
```


