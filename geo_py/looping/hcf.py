# find hcf of two numbers
num1=24
num2=9
for i in range(1,19):
    if num1%i==0 and num2%i==0:
      hcf=i
print(hcf)    

def lcm(num1,num2):
       gcd=hcf(num1,num2)
       res=(num1*num2)/gcd
       
       return res
print(lcm(18,24))
