
# arstrong number
num=371
orginal=num
sum=0
while(num!=0):
    digit=num%10
    cube=digit**3
    sum+=cube
    num=num//10
print(sum)
print("armstrong"if sum==orginal else "not armstrong")    
# if(sum==orginal):
#     print("armstrong number")
# else:
#     print("not armstrong")


