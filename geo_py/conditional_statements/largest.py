# num1=11
# num2=22
# num3=32
# if(num1>num2 and num1>num3):
#     print(f"{num1} is largest")
# elif(num2>num1 and num3):
#     print(f"{num2} is largest")
# # else:
# #     print(f"{num3} is largest")        
# elif(num3>num1 and num3>num2):
#      print(f"{num3} is largest")
# elif(num1==num2 and num1==num3):
#     print("all are equal")
    
    
    
    
    
    
# 

num1=100
num2=20
num3=75
if(num1>num3 and num1<num2):
  if(num2>num3):
     print(num1,num2,num3)
  else:
     print(num1,num3,num2)
     
elif(num2>num1 and num2>num3):
  if(num1>num3):       
     print(num2,num1,num3)
  else:
    print(num2,num3,num1)
    
elif(num3>num1 and num3>num2):
  if(num1>num2):
     print(num3,num1,num2)
  else:
    print(num3,num2,num1) 
    
elif(num1==num2 and num1==num3):
    print("all are equal")  


