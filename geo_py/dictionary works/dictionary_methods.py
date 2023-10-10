student={"name":"geo","course":"django","is_placed":True,"salary":24000}
# to remove
# student.pop("name") # pop
# print(student)
# to return keys
for k in student.keys():# keys
    print(k)
    # for values return
for v in student.values():# value
    print(v)
    # both key and values 
for k,v in student.items(): # items
    print(k,v)       
     # to get the key value
# print(student["name"])
print(student.get("name"))