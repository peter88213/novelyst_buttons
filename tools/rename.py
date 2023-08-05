import glob
import os
import re

for f in glob.iglob('*.png'):
    newName = re.sub('(.+?)Icon\.png', 'nb_\\1.png', f)
    os.rename(f, newName)
