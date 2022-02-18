import os

path = r'G:\my_projects.py'
projectname = 'my_project'
folders = \
[ ['settings', [] ],
  ['mainapp', [] ],
  ['adminapp', [] ],
  ['authapp', [] ]
]

def createFolder(path):
    if not os.path.exists(path):
        os.mkdir(path)

def build(root, data):
    if data:
        for d in data:
            name = d[0]
            path = os.path.join(root, name)
            createFolder(path)
            build(path, d[1])

fullPath = os.path.join(path, projectname)
createFolder(fullPath)

#for f in folders:
 #   folder = os.path.join(fullPath, f)
  #  createFolder(folder)

build(fullPath, folders)
