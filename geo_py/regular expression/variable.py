# from re import*
# variable=input("enter a variable name")# num 1
# #
# rule="[a-zA-Z][0-9a-zA-Z_]*"
# matcher=fullmatch(rule,variable)
# print("Invalid" if matcher==None else "Valid")

#
# rule
# k-m
# must be a digit and that / by 3
# any number of character
from re import *
variable=input("enter variable name")
rule="[k-m][369][\w]*"
matcher=fullmatch(rule,variable)
print("in valid" if matcher==None else "valid")

