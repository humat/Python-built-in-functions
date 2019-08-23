x=input("Enter a number")
y=input("Enter second number")
x=int(x)
y=int(y)
try:
    print(x/y)
except ZeroDivisionError:

    print("y can't be zero.Try another number")
    
