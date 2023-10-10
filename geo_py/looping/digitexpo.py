# cube sum od digits
# step 1-> extract digits
# step 2-> 

num=123
expo=1
while(num!=0):
    digit=num%10
    expo=expo**digit
    num=num//10
print(expo)    