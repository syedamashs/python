def hello(**kwargs):
    #print("hello "+kwargs['first']+' '+kwargs['last'])
   for key,value in kwargs.items():
       print(value,end=' ')
hello(first='bro',middle='dude',last='code')
