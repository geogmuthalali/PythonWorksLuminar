# first 3 digit must be uppercase random alphabets
# 4th place must be alphabet(PCAFHT)
# 5th place any random uppercase
# 4 digits
# one alphabet
from re import *
pan_num=input("enter pan number:")
rule="[A-Z]{3}[PCAFHT]{1}[A-Z]{1}[\d]{4}[A-Z]{1}"
matcher=fullmatch(rule,pan_num)
print("in valid" if matcher==None else "valid")