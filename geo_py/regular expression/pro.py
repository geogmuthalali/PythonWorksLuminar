from re import *
phone_rule="\d{10}"
mail_rule="[a-z][\w\W].[@](gmail)[.]com"
phone_number=[]
mail_id=[]
f=open("C:/Users/GEO/OneDrive/Desktop/geo_py/regular expression/data.txt","r")

for line in f:
    words=line.rstrip("\n").split(" ")
    for w in words:
        p_matcher=fullmatch(phone_rule,w)
        m_matcher=fullmatch(mail_rule,w)
        if p_matcher!=None:
            phone_number.append(w)
        elif m_matcher!=None:
            mail_id.append(w)
print(phone_number)
print(mail_id)            
