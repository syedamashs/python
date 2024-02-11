with open('new.txt','w') as a:
   a.write('hi how are you\n')
with open('new.txt','a') as a:
    a.write('hoo')



with open('new.txt') as file:
    print(file.read())
