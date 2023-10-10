# args -> *
#  * -> tuple
# variable length argument method
def product(*args):
    res=1
    for n in args:
        res*=n
    print(res)

product(2,4)    
product(2,3,4,5)
#
def greeting(*args):
    print(f"hello {args[0]} app user {args[1]}")
greeting("good afternoon","geo")    


# kwargs -> **
# ** -> dictionary
def greeting(**kwargs):
    print(f"hello {kwargs.get('msg')} app user {kwargs.get('user_name')}")
greeting(msg="good morning",user_name="geo")  
#
def dispatch_order(**kwargs):
    print(f"hello user {kwargs.get('name')} your order {kwargs.get('code')}{kwargs.get('item')} is ready to {kwargs.get('status')}")

dispatch_order(item="ucb shirt",code="123bc",status="deliver",name="vijay")