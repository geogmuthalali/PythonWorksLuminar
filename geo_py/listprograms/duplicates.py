arr=[5,2,5,3,4,1,2]
#FIND DULIPCATES
arr.sort()
duplicate_list=[]
for i in range(0,len(arr)-1):
    current=arr[i]
    next=arr[i+1]
    
    if current==next:
        if current not in duplicate_list:
            duplicate_list.append(current)
 
print(duplicate_list)            
        
 
 
arr=[1,3,4,6,5,15]
#find least +ve missing integer
arr.sort()  
arr.remove(15)
print(arr)
for a in range(0,len(arr)-1):
    current=arr[a]
    next=arr[a+1]
    
    if next-current!=1:
        print(current+1)
        break