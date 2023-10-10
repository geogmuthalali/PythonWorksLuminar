#
def swap_num(fn):
    def inner_fun(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return inner_fun  
def smart_div(fn):
    def wrapper(n1,n2):
        if n2==0:
            print("Div by 0 not possible")  
            return
        return fn(n1,n2)
    return wrapper
@swap_num
def sub(n1,n2):
    return n1-n2
@swap_num
@smart_div
def div(n1,n2):
    return n1/n2 

print(sub(2,6))
print(div(2,0))

#
def decorator1(fn):
    def wrapper():
        print("decorator 1 before calling orginal fn")
        result=fn()
        print("decorator 1 after calling orginal fn")
        return result
    return wrapper
def decorator2(fn):
    def wrapper():
        print("decorator 2 before calling orginal fn")
        result=fn()
        print("decorator 2 after calling orginal fn")
        return result
    return wrapper

@decorator1
@decorator2
def orginal_function():
    print("this is the orginal fn")

orginal_function()    
