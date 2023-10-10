# start with kl
# 2 digit
# alphabet min 1 max2
# digit 4
from re import *
vehicle_number=input("enter vehicle number : ")
rule="(KL)-[\d]{2}-[A-Z]{1,2}-[\d]{4}"
matcher=fullmatch(rule,vehicle_number)
print("in valid" if matcher==None else "valid")