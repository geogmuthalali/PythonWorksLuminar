class employee:
    id:int
    name:str
    gender:str
    department:str
    salary:int

    def create(self,id,name,gender,dept,salary):
         self.id=id
         self.name=name
         self.gender=gender
         self.department=dept
         self.salary=salary
    def get(self):
         print(self.id,self.name,self.gender,self.department,self.salary)

emp1=employee()
emp1.create(100,"aswan","male","it",55000) 

emp2=employee()
emp2.create(101,"akhil","male","it",50000)

emp3=employee()
emp3.create(102,"parvathy","female","ca",45000)
emp1.get()
emp2.get()
emp3.get()