# print all vowels using re
from re import *
text="goodmorning #sachin001"
#     0123456789
Pattern="[aeiou]"
Pattern="[^aeiou\W\d]" # to find consonents
matcher=finditer(Pattern,text)
for m in matcher:
    print(m.start(),m.groups())

   
