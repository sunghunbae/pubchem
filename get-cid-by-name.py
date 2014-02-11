#!/usr/bin/env python
import pycurl
import cStringIO
import urllib
import sys

url="http://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/cids/TXT"
hdr=['Accept: text/plain','Content-Type: application/x-www-form-urlencoded']

name="N6-methyladenosine"

post = 'name=' + urllib.quote_plus(name)

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
  cids = (buf.getvalue()).strip() # multiple lines
  cids = cids.splitlines()[0] # first result
  buf.close()
  print name, cids
except pycurl.error :
  print name, "error"

sys.stdout.flush()
