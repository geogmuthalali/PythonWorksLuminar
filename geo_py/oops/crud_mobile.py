mobiles=[
    {"id":1,"name":"OneplusNordCE3Lite","brand":"oneplus","price":19999},
    {"id":2,"name":"Realme11pro","brand":"realme","price":29999},
    {"id":3,"name":"Oneplus11","brand":"oneplus","price":61699},
    {"id":4,"name":"iQOO9pro","brand":"iqoo","price":44990},
    {"id":5,"name":"AppleIphone14pro","brand":"xiaomi","price":119999},
    
]

# add754936
def add_device(*args,**kwargs):
    mobiles.append(kwargs)
    add_device(id=6,name="AsusROGphone7ulti",brand="asus",price=99999)
print(mobiles)
# retrieve
def retrieve_device(id=None,*args,**kwargs):
    obj=[m for m in mobiles if m.get("id")==id]
    return obj
# print(retrieve_device(id=2))
# delete
def delete_device(id=None,*args,**kwargs):
    obj=[m for m in mobiles if m.get("id")==id][0]
    mobiles.remove(obj)
# delete_device(id=1)  
# print(mobiles)
#
def update_device(id=None,*args,**kwargs):
    obj=[m for m in mobiles if m.get("id")==id][0]
    obj.update(kwargs)
update_device(id=4,name="NothingPhone1",brand="nothing")  
# print(retrieve_device(id=4))
