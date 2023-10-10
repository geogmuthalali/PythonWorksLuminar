lst1=[10,11,12,13,16]
lst2=[12,13,14,20,21]
                              # (big O notation)
# for n in lst1:               # o()t -> Time complexity
#     if n in lst2:            # o()s ->space complexity
#         print(n)
# for n1 in lst1:
#     if n1 in lst2:
#         print("common",n1)
 
p1,p2=0,0       
lst1.sort()
lst2.sort()

while p1<len(lst1) and p2<len(lst2):
    if lst1[p1]==lst2[p2]:
        print("common",lst2[p2])
        p1+=1
    elif lst1[p1]<lst2[p2]:
        p1+=1
    else:
        p2+=1                