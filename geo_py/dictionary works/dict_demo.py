# # DICTIONARY
# duplicate key is not allowed
person={"name":"geo","age":"21","gender":"maLe"}
print(person["name"])
print(person["gender"])
if "salary" in person:
      person["salary"]+=2000
else:
      person["salary"]=30000
print(person)      
# mobile
mobile={"name":"oneplus nord 1","brand":"oneplus","price":38000}
print(mobile["name"])
## disc_obj[key]=value
mobile["display"]="amoled"
print(mobile)
# #to check whether a key present
if "offer" in mobile:
    print("offer key is present")
else:
    print("not exist") 
    # if offer is present add offer+50 or add offer as 50
if "offer" in mobile:
        mobile["offer"]+=50
else:
        mobile["offer"]=50
print(mobile)        
# hotel
orders=["veg meals","fish meals","veg meals","fish meals","vb","cb","bb","cb","fried rice"]
order_count={}
for item in orders:
      if item in order_count:
            order_count[item]+=1
      else:
            order_count[item]=1
print(order_count)  
# enquries          
enquries=["django","testing","django","big data","testing","django","aws","django"]
enquries_count={}
for en in enquries:
      if en in enquries_count:
            enquries_count[en]+=1
      else:
            enquries_count[en]=1
print(enquries_count)    
#carrot
text="carrot"
wc={}
for ch in text:
      if ch in wc:
          wc[ch]+=1
      else:
            wc[ch]=1
print(wc)
#
text="ABCDAB"
#FIRST RECURSIVE NUMBER
txt={}
for ch in text:
      if ch in txt:
            print(ch,"is the first recursive character")
            break
      else:
            txt[ch]=1
#
text="ABBCCDEF"
#find all non recursive character from text            
wc={}
for ch in text:
      if ch in wc:
          wc[ch]+=1
      else:
            wc[ch]=1
print(wc)
for k,v in wc.items():
      if v==1:
        print(k)
 
     
                
