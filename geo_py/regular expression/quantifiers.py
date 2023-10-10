from re import *
text="aabbaaac"
#     01234567
# pattern="a+" # + one or more occurance of 'a'
# pattern="a*" # zero or more occurance of 'a'
pattern="a{1,2}" # a{min,max}
matcher=finditer(pattern,text) 
for m in matcher:
    print(m.start(),m.groups())

#"[a-zA-Z0-9]*"    