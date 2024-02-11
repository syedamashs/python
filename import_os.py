import os

path ="//home//amash//Desktop//New"

if os.path.exists(path):
    print("location exists")
    if os.path.isfile(path):
        print("its is a file")
    elif os.path.isdir(path):
        print("its is a directory!")
else:
    print("no location")
