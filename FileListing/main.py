import os
from os import path
import re

user_path = input('Enter path of directory:')

dict = {}
try:
    if os.path.isdir(user_path):
        files = os.listdir(user_path)
        for file in files:
            if os.path.isfile(user_path+'/'+file):
                pattern = re.search(r'\.[A-Za-z0-9]+$', file)
                extension = pattern.group(0) if pattern else ""

                if extension in dict:
                    dict[extension] += os.path.getsize(user_path+'/'+file)
                else:
                    dict[extension] = os.path.getsize(user_path+'/'+file)
        print(dict)
    else:
        raise NotADirectoryError

except NotADirectoryError as e:
    print('Not a directory')

