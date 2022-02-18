
#path = r'G:\my_project.py'

import os

for directory, subdirectory, folders, files in os.walk("G:/my_project.py"):
    print(folders.st_size)