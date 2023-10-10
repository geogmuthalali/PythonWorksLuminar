# binary search
# worst case

lst=[12,13,3,4,14,16,18]
lst.sort()
element=16
low=0
upp=len(lst)-1
is_found=False
while(low<=upp):
    mid=(low+upp)//2

    if element==lst[mid]:
      is_found=True
      break

    elif element<lst[mid]:
      upp=mid-1
      
    elif element>lst[mid]:
       low=mid+1

print(is_found)        
 

