from json import load
path="C:\\Users\\GEO\\Desktop\\geo_py\\countries\\countries.json"

with open(path,encoding="utf-8") as f:
    countries=load(f)
print(len(countries)) 
# print all country names
country_names=[ c.get("name") for c in countries ]
print(country_names)
# capital of china
country_capital=[c.get("capital") for c in countries if c.get("name")=="China"]
print(country_capital)
# capital of india
capitalofindia=[c.get("capital") for c in countries if c.get("name")=="India"]
print(capitalofindia)
# 
# language=[c.get("name") for c in countries if c.get("language")=="english"]
# print(language)
#
# print regions
# regions={c.get("region") for c in countries }
regions=[c.get("region") for c in countries ]
print(set(regions))
country_borders=[c.get("borders") for c in countries if c.get("name")=="India"][0]
print(country_borders)

border_name=[c.get("name") for c in countries  if c.get("alpha3Code") in country_borders]
print(border_name)
#
# print independent country name
independent_country=[c.get("independent") for c  in countries if c.get("name")=="Sri Lanka"]
print(independent_country)
# currency name of India
currency_details=[c.get("currencies") for c in countries if c.get("name")=="India"][0][0]
print(currency_details)
#
country_currencies=[c for c in countries if "currencies" in c]
currencies=[c.get("currencies")[0].get("symbol") for c in country_currencies for cur in c.get("currencies")]
wc={}
for c in currencies:
    if c in wc:
        wc[c]+=1
    else:
        wc[c]=1
# print(wc)
print(max( (v,k)for k,v in wc.items()))        
# print(currencies)
# regular expression
