import os, re

os.chdir(r"/Users/onno/Projects/stuff/")
for f in os.listdir():
    if re.match(r"^\d\d\d\d-\d\d-\d\d.ipynb$", f) and os.stat(f).st_size == 68:
        os.remove(f)
