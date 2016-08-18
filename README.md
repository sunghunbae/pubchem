PubChem REST service
====================

The PubChem database provides the REST-style version of PUG
(Power User Gateway), a web interface for accessing PubChem data and services.

https://pubchem.ncbi.nlm.nih.gov/pug_rest/PUG_REST.html

### generate 3D SDF using openbabel

```
$ obabel -:"CNC1=NC=NC2=C1N=CN2C3C(C(C(O3)CO)O)O" -O ob-102175.sdf -h -p --gen3d
```

### generate SVG using openbabel
```
$ obabel -:"CNC1=NC=NC2=C1N=CN2C3C(C(C(O3)CO)O)O TITLE" -O ob-102175.svg
```
