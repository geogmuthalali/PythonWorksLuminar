text="malayalam"
count=len(text)-1
p_str=" " 
for i in range(count,-1,-1):
    p_str+=text[i]
    
print("palindrome" if text==p_str else "not palindrome")    

