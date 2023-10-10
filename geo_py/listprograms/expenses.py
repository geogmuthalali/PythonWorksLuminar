expenses=[12000,13000,14000,11000,25000,28000,21000]

#maximum

max_exp=expenses[0]
for e in expenses:
    if e>max_exp:
        max_exp=e
print(max_exp)  
      
#minimum

min_exp=expenses[0]
for e in expenses:
    if e<min_exp:
        min_exp=e
        
print(min_exp)   
 
#ascending & decending order

srt_exp=sorted(expenses,reverse=False)
print(srt_exp)
desc_exp=sorted(expenses,reverse=True)
print(desc_exp)