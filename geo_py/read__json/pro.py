from json import  load
path="C:\\Users\\GEO\\Desktop\\geo_py\\read_json\\data.json"
with open(path) as f:
    records=load(f)

# print(records)
fw_name=[f.get("names") for f in records]
print(fw_name)

top_fw=max(records,key=lambda d:d.get("rating"))
print(top_fw)