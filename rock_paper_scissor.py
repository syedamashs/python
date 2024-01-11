import random
a=['rock','paper','scissor']
u=0
c=0
for i in range(5):
 c=input("enter rock or paper or scissor:")
 while c not in a:
     c=input("enter rock or paper or scissor:")
 b=random.choice(a)
 print(b)
 if (c=='rock' and b=='scissor') and (c=='paper' and b=='rock') and (c=='scissor' and b=='paper') :
     print("you won")
     u=u+1
 elif c==b :
     print("its a tie")
 else :
     print("you lose")
     c=c+1

if u>c :
    print("player wins")
elif c>u :
    print("computer wins")
elif c==u :
    print("its a tie")
