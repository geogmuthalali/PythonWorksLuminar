# text="hello hai goodmorning zython hi"
# #longest word
# words=text.split()
# srt=sorted(words,reverse=True,key=lambda w:len(w))
# print(srt)
# l_words=max(words,key=lambda w:len(w))
# print(l_words)
# # len_words=min(words,key=lambda w:len(w))
# # print(len_words)
#
items=[
    {"id":1,"name":"sugar","price":40,"avl_quality":10},
    {"id":2,"name":"milk","price":28,"avl_quality":100},
    {"id":3,"name":"tea powder","price":49,"avl_quality":50},
    {"id":4,"name":"tomato","price":160,"avl_quality":0},
    {"id":5,"name":"carrot","price":60,"avl_quality":0},
    {"id":6,"name":"potatto","price":35,"avl_quality":20},
    {"id":7,"name":"oreo","price":40,"avl_quality":50},
    {"id":8,"name":"hide and seek","price":50,"avl_quality":30}
]
#all names
all_names=[i.get("name") for i in items]
print(all_names)

#in stock
in_stock=[i.get("name") for i in items if i.get("avl_quality")>0]
print(in_stock)

#price below 50
price_filterfifity=[i.get("name") for i in items if i.get("price")<45]
print(price_filterfifity)

#range
range_filter=[i.get("name") for i in items if i.get("price") in range(20,51)]
print(range_filter)

# price
# oreo_price=[i.get("price") for i in items if i.get("name")=="oreo"]
# print(oreo_price)

# price change
oreo_data=[i for i in items if i.get("name")=="oreo"]
oreo_data[0]["price"]=50

print(items)

oreo_price=[i.get("price") for i in items if i.get("name")=="oreo"]
print(oreo_price)
