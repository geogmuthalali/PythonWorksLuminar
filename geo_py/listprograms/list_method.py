#List methods...
users=["Mohalal","Mammootty","Dq","Nivin","Fahadh",""]
#          0          1        2      3
users.append("Tovino") #append only add objects to the end of the list. ->to add
# users.pop(3) #if no object is given it remove the last object. -> to remove 
print(users.index("Dq")) # to find the location of the specified object.
print(users.count("Nivin")) # to find the how many time the object occured. 
users.sort(reverse=True) #to sort the objects -> asc/des
# users.clear() # to clear the list
users.remove("Mohalal") #to remove a particular object
print(users)
if("sreenivasan" in users):
    print("Present")
else:
    print("not Present")
    if "sreenivasan" not in users:  
        users.append("sreenivasan")
print(users)       