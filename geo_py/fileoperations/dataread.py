f=open("C:/Users/Admin/Desktop/geo_py/fileoperations/data.txt","r")
           #       read
# for line in f:
#     print(line)

           #      append
    # step 1       
# word=[]
# for line in f:
#     word.append(line.rstrip("\n"))
#     print(word) 
    # step 2
word=[line.rstrip("\n") for line in f]
print(word)   