# variable length argument method
def product(*args):
    res=1
    for n in args:
        res*=n
    print(res)

product(2,4)    
product(2,3,4,5)
#

# # *
# def greeting(*args):
#     print(f"hello {args(0)} app user{args(1)}")
# greeting("good morning","geo")    
# #

# **

# def greeting(**kwargs):
#     print(f"hello {kwargs.get(0)} app user {kwargs.get(1)}")
# greeting(msg="good morning",user_name="geo")  

# def dispatch_order(**kwargs):
#     print(f"hello user {kwargs.get('name')} your order {kwargs.get('code')}{kwargs.get('item')} is ready to {kwargs.get('status')}")

# dispatch_order(item="ucb shirt",code="123bc",status="deliver",name="vijay")


#method overloading

# same method name different number of parameters
class calculator:
    def add(self,n1,n2):
        print(n1+n2)
    def add(self,n1,n2,n3):
        print(n1+n2+n3)    
obj=calculator()
obj2=calculator()
obj.add(11,22,33)        
obj2.add(2,3,4,)