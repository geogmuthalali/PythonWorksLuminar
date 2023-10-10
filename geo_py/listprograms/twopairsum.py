lst=[2,3,4,5]
sum=8
# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         cur_sum=lst[i]+lst[j]
#         if cur_sum==sum:
#             print("pair",lst[i],lst[j])

     
count=1

low=0
upp=len(lst)-1
while(low<upp):
    cur_sum=lst[low]+lst[upp]
    if cur_sum==sum:
        print(lst[low],lst[upp])
        break
    elif(cur_sum<sum):
        low+=1
    else:
        upp-=1