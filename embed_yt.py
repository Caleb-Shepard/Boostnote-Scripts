#!/usr/local/bin/python3
from sys import argv

iframe_prefix = '<iframe width="560" height="315" src="'
iframe_suffix = '" frameborder="0" allowfullscreen></iframe>'
print(iframe_prefix + argv[1] + iframe_suffix)
