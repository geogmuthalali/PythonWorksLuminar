num1=11
num2=22
num3=33

def largest(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(f"{num1} is largest")
    elif num2>num3 and num2>num1:
        print(f"{num2} is largest")
    elif num3>num1 and num3>num2:
        print(f"{num3} is largest")
    else:
        print("all are equal")
largest(num1,num2,num3)                