import fnmatch
import os
import re
import shutil
from sys import argv

path = argv[1]
os.chdir(path)
cwd = os.getcwd()
toPath = path + "_unpacked"
folder_names = os.listdir(cwd)
dictionary = {}

for (dirpath, dirnames, filenames) in os.walk(path):
    for filename in fnmatch.filter(filenames, '*.mtl'):
        filenameNoExt = os.path.splitext(filename)[0]
        dictionary[filenameNoExt] = [filename]
        dictionary[filenameNoExt].append(filenameNoExt+".obj")
        with open(os.path.join(path, filename)) as file:
            for line in file.readlines():
                regex = re.compile(r" (.*?.jpg|bmp|png)")
                a = re.search(regex, line.rstrip())
                if a:
                    dictionary[filenameNoExt].append(a.group(1))
                else: pass

for key, value in dictionary.items():
    if not os.path.exists(key):
        os.makedirs(key)
    for i in value:
        shutil.copy(i, key)
        print(value)
