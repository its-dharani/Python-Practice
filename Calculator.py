a=int(input("Enter first number: "))
b=int(input("Enter Second number: "))
op=input("Enter the operation: ")

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

if op=="+":
    print("The sum is:",add(a,b))
elif op=="-":
    print("The difference is:",sub(a,b))
elif op=="-":
    print("The product is:",mul(a,b))
elif op=="/":
    print("The quotient is:",div(a,b))
else:
    print("Operation cannot be done!")