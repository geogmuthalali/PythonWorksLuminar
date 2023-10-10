from re import *
# password
# atleast one uppercase
# alteast one speacil character
# min 8 characters
password="password@123"
rule="(?=.*[A-Z])(?=.*[\W])(?=.*[\d]).{8,}"
matcher=fullmatch(rule,password)
print("invalid" if  matcher !=None else "valid")
