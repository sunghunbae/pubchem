#!/usr/bin/env python
#
# written by Sung-Hun Bae
#

import subprocess
import os

for f in sorted(os.listdir('.')):
  if f.endswith('.sdf'):
    proc=subprocess.Popen(['obabel','-isdf',f,'-osmi'],
      stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,err = proc.communicate()
    print f,
    try:
      print out.splitlines()[0].rstrip().split()[0]
    except IndexError: 
      print "Error"
