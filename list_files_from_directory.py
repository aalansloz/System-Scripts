#!/usr/bin/env python
from __future__ import print_function
import os
 
path = '.'

f= open("files.txt", "a")
files = os.listdir(path)
for name in files:
    print(name)
    f.write(name)
    f.write('\n')
f.close()
