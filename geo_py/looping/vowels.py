# text="abcdefghijklmnopqrstuvwxyz"
# for ch in text:
#     if ch in["a","e","i","o","u"]:
#    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
    #    print(ch)
       
# membership operators       
       
text="abcdefghijklmnopqrstuvwxyz"
v_count=0
c_count=0
for ch in text:
    if ch in["a","e","i","o","u"]:
         v_count+=1
    else:
        c_count=c_count+1
        
print("number of vowels:",v_count)
print("number of constants",c_count)
               