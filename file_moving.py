import os

source="New"#new.txt both here and below the place
destination="//home/amash//Desktop//New"

try:
   if os.path.exists(destination):
       print("there is already a fle there  with the same name")
   else:
       os.replace(source,destination)
       print(source+" was moved")


except FileNotFoundError:
    print(source+" was not found")
