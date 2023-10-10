# selling price
# # 50 20%
# def get_discount_price(actual_price,discount):
#    selling_price=actual_price-(actual_price*discount)/100
#    return selling_price
# print(get_discount_price(50,10))

# least common multiple

# def lcm(num1,num2):
#      max=num1 if num1>num2 else num2
#      flag=True
#      while(flag):
#         if max%num1==0 and max%num2==0:
#            print(f"lcm of {num1}","lcm of {num2}")
#            break
#         else:
#          max=+1
# lcm(18,24)       
#
square=lambda n:n**2
cube=lambda n:n**3
max_two=lambda n1,n2:n1 if n1>n2 else n2
min_two=lambda n1,n2:n1 if n1<n2 else n2     

print(square(10))
print(cube(6))
print(max_two(2,4))
print(min_two(2,4))
       
   