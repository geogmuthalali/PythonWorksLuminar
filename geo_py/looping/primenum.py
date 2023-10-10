num=int(input("enter number to check prime or not : "))
is_prime=True

for i in range(2,num):
    if num%i==0:
     is_prime=False
     break
print(is_prime)     
      
       