import shutil

shutil.copyfile('new.txt','/home/amash/Desktop/copy.txt') 
shutil.copy('new.txt','/home/amash/Desktop/copy.txt')
shutil.copy2('new.txt','/home/amash/Desktop/copy.txt')

with open('copy.txt') as a:
    print(a.read())
