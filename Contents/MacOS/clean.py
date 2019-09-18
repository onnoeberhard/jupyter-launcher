import os, re

os.chdir(r"/Users/onno/Projects/stuff/")
for f in os.listdir():
    if re.match(r"^\d{4}-\d\d-\d\d(-sage)?.ipynb$", f) and os.stat(f).st_size in (68, 555, 550):
        os.remove(f)
