a=8
b=0
try:
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print(e)
    print("hey dont divide by zero!!")