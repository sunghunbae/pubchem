#!/usr/bin/env python
import sys

prefix = 'a-'

for bigsdffile in sys.argv[1:]:
  try:
    f = open (bigsdffile, 'r')
  except IOError:
    sys.exit(1)

  lineNum = 0
  sdfNum = 0

  for line in f.readlines() :
    line = line.strip()
    lineNum += 1

    if lineNum == 1 : 
      sdfNum += 1
      print "%6d %s" % (sdfNum,line)
      sdf = open (prefix+line+".sdf", 'a')
      sdf.write(line+"\n")

    if line == "$$$$"  : 
      lineNum = 0
      sdf.close()

  f.close()
