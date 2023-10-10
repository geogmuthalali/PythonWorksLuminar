class student:
    id:int
    name:str
    age:int
    gender:str
    department:str

    def __init__(self,id,name,age,gender,department):
        self.id=id
        self.name=name
        self.age=age
        self.gender=gender
        self.department=department

    def get(self):
        print(self.id,self.name,self.department)
    
    def __str__(self):
        return self.name+str(self.age)   
        

obj=student(100,"aswan",20,"male","computer science")
obj2=student(102,"parvathy",20,"female","chartered accountant")
print(obj)
print(obj.name,obj.department)
print(obj2.name,obj2.age)




