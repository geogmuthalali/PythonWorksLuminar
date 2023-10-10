class Hotel:
    items=[
    {"id":100,"name":"cb","price":160},
    {"id":101,"name":"vb","price":140},
    {"id":102,"name":"ghhe roast","price":120},
    {"id":103,"name":"afm","price":130},
    {"id":104,"name":"cf","price":90},
    {"id":105,"name":"porotta","price":10},

    ]
#create
    def create(self,*args,**kwargs):
       self.items.append(kwargs)
       return f"{kwargs} is created"
# retrieve    
    def retrieve(self,id=None,*args,**kwargs):
        obj=[i for i in self.items if i.get("id")==id][0]
        return obj
# update    
    def update(self,id=None,*args,**kwargs):
        obj=self.retrieve(id=id)
        old_obj=obj.copy()
        obj.update(kwargs)
        return f"{old_obj} has been updated as {obj}"
# destroy    
    def destroy(self,id=None,*args,**kwargs):
        obj=[i for i in self.items if i.get("id")==id][0]
        self.items.remove(obj)
        return f"{obj} has been removed"

obj=Hotel()
# print(obj.create(id=106,name="cm",price=180))
# print(obj.retrieve(id=101))
print(obj.update(id=102,name="GHEE ROAST"))
# print(obj.destroy(id=102))