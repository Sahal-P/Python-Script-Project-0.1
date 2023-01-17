import os 
import json
import shutil
from subprocess import PIPE, run
import sys

a = "game "
b = "home"

c = os.path.join(a,b)

for root, dirs, files in os.walk(c):
    print(root)
    print(dirs)
    print(files)
    
