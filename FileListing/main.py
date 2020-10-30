import os
from os import path
import re

user_path = input('Enter path of directory:')

dict = {}
files = os.listdir(user_path)

if str(os.path.isdir('user_path')):

    for file in files:
        pattern = re.search(r'\.[A-Za-z0-9]+$', file)
        extension = pattern.group(0) if pattern else ""

        if extension in dict:
            dict[extension] += os.path.getsize(user_path+'/'+file)
        else:
            dict[extension] = os.path.getsize(user_path+'/'+file)

else:
    print('Input user path is not correct ')
    exit()

print(dict)
