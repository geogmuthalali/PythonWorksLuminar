from re import *

text="python @ 123"
#     0123456789
# Pattern="[a-z]" # check for all  lowercase alphabets
# Pattern="[A-Z]" # check for all  uppercase alphabets
# Pattern="[a-zA-Z]" #  all alphabets
# Pattern="[0-9]"  # numeric
Pattern="[a-zA-Z0-9]" # alpha numeric

matcher=finditer(Pattern,text)
#
for m in matcher:
    print(m.start(),m.group())

#
from re import *
text="ababa123ABC@"
#     0123456789
# Pattern="\d" #"[0-9]" -> same as the to find digit
# Pattern="\D" # "[^0-9]" -> non numeric to find
# Pattern="\w" # "[a-zA-Z0-9]"  ->  alpha numeric
Pattern="\W" # "[^a-zA-Z0-9]" ->  non alpha numeric
matcher=finditer(Pattern,text)
for m in matcher:
    print(m.start(),m.groups())

 
