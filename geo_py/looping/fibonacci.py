prev=0
curr=1
print(prev)
print(curr)
start=1
while(start <=9):
    fib=prev+curr
    print(fib)
    perv=curr
    curr=fib
    start+=1    
