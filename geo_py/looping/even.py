# print all the numbers which are divisible by 3 and 5 upto given range
i1=int(input("enter the start number : "))
i2=int(input("enter the end number : "))
while(i1<=i2):
    if(i1 %3==0 and i1 %5==0):
        print(i1)
    i1+=1