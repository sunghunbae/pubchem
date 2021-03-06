#!/usr/bin/env python
import pycurl
import cStringIO
import urllib
import sys

url="http://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/sids/TXT"
hdr=['Accept: text/plain']

cid = '102175'
post = 'cid=' + cid

try:
  buf = cStringIO.StringIO ()
  c = pycurl.Curl()
  c.setopt(c.URL, url)
  c.setopt(c.HTTPHEADER, hdr)
  c.setopt(c.POSTFIELDS, post)
  c.setopt(c.CONNECTTIMEOUT, 60)
  c.setopt(c.TIMEOUT, 60)
  c.setopt(c.WRITEFUNCTION, buf.write)
  c.perform()
  sids = ((buf.getvalue()).strip()).split()
  buf.close()
  print cid, len(sids), sids

except pycurl.error :
  print cid, 0, "error"

sys.stdout.flush()
