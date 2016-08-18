#!/usr/bin/env python

import cStringIO as StringIO
import pycurl
import urllib
import json

def PubchemRequest (url, hdr, post=''):
  try:
    buf = StringIO.StringIO ()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.HTTPHEADER, hdr)
    if post:
      c.setopt(c.POSTFIELDS, post)
    c.setopt(c.CONNECTTIMEOUT, 60)
    c.setopt(c.TIMEOUT, 60)
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.perform()
    response = buf.getvalue().strip()
    buf.close()
    return response
  except pycurl.error:
    return "CurlError"

def Synonyms ( name='', cid='' ):
  base="https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/"
  op="/synonyms/JSON"
  if name:
    url=base+"name/"+name+op
  elif cid:
    url=base+"cid/"+cid+op
  else:
    return None
  hdr=['Accept: application/json','Content-Type: application/json']
  response = PubchemRequest(url,hdr)
  if response:
    return json.loads( response )
  else:
    return None

def getCAS ( cidList=[] ) :
  url="https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/synonyms/JSON"
  hdr=['Accept: application/json','Content-Type: application/json']
  cids=[ urllib.quote_plus(item) for item in cidList ]
  post="cids="+ ','.join(cids)
  response= PubchemRequest(url,hdr,post)
  return json.loads( response )

def PropertyTablePost ( name=[], cid=[] ):
  base="https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/"
  op="/property/MolecularWeight,MolecularFormula,IUPACName,IsomericSMILES/JSON"
  hdr=['Accept: text/plain','Content-Type: application/x-www-form-urlencoded']
  if len(name) > 0:
    url=base+"name"+op
    post='name=' + urllib.quote_plus(','.join(name))
    response = PubchemRequest(url,hdr,post)
  elif len(cid) > 0:
    url=base+"cid"+op
    post='cid=' + urllib.quote_plus(','.join(cid))
    response = PubchemRequest(url,hdr,post)
  else:
    return None
  return json.loads( response )

def PropertyTable ( name='', cid='' ):
  base="https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/"
  op="/property/MolecularWeight,MolecularFormula,IUPACName,IsomericSMILES/JSON"
  if name:
    url=base+"name/"+name+op
  elif cid:
    url=base+"cid/"+cid+op
  else:
    return None
  hdr=['Accept: application/json','Content-Type: application/json']
  response = PubchemRequest(url,hdr)
  return json.loads( response )

def getCID ( name='', smiles='' ):
  cid=None
  hdr=['Accept: text/plain','Content-Type: application/x-www-form-urlencoded']
  if name:
    url="http://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/cids/TXT"
    post = 'name=' +  urllib.quote_plus(name)
    response = PubchemRequest ( url, hdr, post )
    try:
      cid=int(response)
    except:
      cid=None
  if smiles:
    url="http://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/cids/TXT"
    post = 'smiles=' +  urllib.quote_plus(smiles)
    response = PubchemRequest ( url, hdr, post )
    try:
      cid=int(response)
    except:
      cid=None

  if cid:
    return cid
  else:
    return -1

def getCIDPost ( name=[], smiles=[] ):
  base="https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/"
  op="/property/MolecularWeight,MolecularFormula,IUPACName,IsomericSMILES/JSON"
  hdr=['Accept: text/plain','Content-Type: application/x-www-form-urlencoded']
  if len(name) > 0:
    url=base+"name"+op
    post='name=' + urllib.quote_plus(','.join(name))
    response = PubchemRequest(url,hdr,post)
  elif len(smiles) > 0:
    url=base+"smiles"+op
    post='smiles=' + urllib.quote_plus(','.join(smiles))
    response = PubchemRequest(url,hdr,post)
  else:
    return None
  return json.loads( response )
