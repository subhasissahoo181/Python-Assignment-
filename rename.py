# Write a python program to rename a file to "renamed-by-python.txt"

import os
oldname = "ch-9/sample.txt"
newname = "ch-9/renameed_by_python.txt"

with open(oldname) as f:
    content = f.read()
with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)