#!/usr/bin/env python

from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors

def parseSDF ( filename ):
  obj={}
  with open(filename,'r') as f:
    num=0
    previousLine='$$$$'
    block=''
    for line in f:
      if previousLine.startswith('$$$$'):
        num += 1
        obj[num]={'title': line.strip()}
        block += line
      elif previousLine.startswith('>'):
        val = line.strip()
        obj[num][key] = val
      elif line.startswith('>'):
        key = line.strip().split()[1]
        key = key.replace('<','')
        key = key.replace('>','')
      elif line.startswith('$$$$'):
        obj[num]['MolBlock']=block
        try:
          m = Chem.MolFromMolBlock ( block )
          obj[num]['IsomericSMILES'] = Chem.MolToSmiles (m, isomericSmiles=True)
          obj[num]['MolecularFormula'] = rdMolDescriptors.CalcMolFormula (m)
          obj[num]['MolecularWeight'] = Descriptors.MolWt (m)
        except:
          pass
        block=''
      else : # MDL MOL BLOCK
        block += line
      previousLine=line
    return obj
