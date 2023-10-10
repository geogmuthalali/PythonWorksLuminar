def deorator1(f):
    def inner():
        x = f()
        return x*x
    return inner

def deorator2(f):
    def inner():
        x = f()
        return 2*x
    return inner
@deorator2
@deorator1
def num():
    return 10

print(num())