def add(*matter):      #makes the numbers into tuple
    matter=list(matter)
    matter[0]=0
    sum=0
    for i in matter:
        sum+=i
    return(sum)

print(add(1,4,3,2))

