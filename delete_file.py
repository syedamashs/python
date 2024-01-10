import os
import shutil

os.remove('new.txt')
os.rmdir('folder')#empty folder
shutil.rmtree('folder')#folder which has files
