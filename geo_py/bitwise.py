# bitwise operators
# &
# |
# ^

# 0 0 => 0
# 0 1 => 0
# 1 0 => 0
# 1 1 => 1

# 1 & 2 => 0001 & 0010
#                      0000 => 0
# 1 | 2 => 0001 | 0010
#                      0011 => 3
# 1 ^ 2 => 0001 ^ 0010
#                     0011 => 3

print("bitwise and : ",1&2)
print("bitwise or : ",1|2)
print("bitwise not : ",~1)
print("bitwise not : ",~2)
print("bitwise not : ",~3)
print("bitwise not : ",~-1)
print("bitwise not : ",~-2)
print("bitwise not : ",~-3)
             