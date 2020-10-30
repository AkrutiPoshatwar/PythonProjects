import os
import re

user_path = input('Enter path of directory:')

dict = {}
files = os.listdir(user_path)

for file in files:
    pattern = re.search(r'\.[A-Za-z0-9]+$', file)
    extensions = pattern.group(0) if pattern else ""
    dict.update({extensions:0})

    if extensions in file:
       dict.update({extensions: dict[extensions] + os.path.getsize(file) })


print(dict)
