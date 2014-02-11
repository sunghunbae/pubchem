PubChem Power User Gateway (PUG) REST service
=============================================

PubChem Database provides the REST-style version of PUG, a web interface 
for accessing PubChem data and services.

https://pubchem.ncbi.nlm.nih.gov/pug_rest/PUG_REST.html


OpenBabel
=========

### generate 3D SDF using openbabel

```
$ obabel -:"CNC1=NC=NC2=C1N=CN2C3C(C(C(O3)CO)O)O" -O ob-102175.sdf -h -p --gen3d
```

### generate SVG 
```
$ obabel -:"CNC1=NC=NC2=C1N=CN2C3C(C(C(O3)CO)O)O TITLE" -O ob-102175.svg
```
