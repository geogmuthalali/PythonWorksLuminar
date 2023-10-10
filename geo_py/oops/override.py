# # override

# class Car:
#     def start(self):
#         print("key start")
#     def break_type(self):
#         print("drum break")
#     def transmission(self):
#         print("manual")
# class Ambassador(Car):    #Ambassador is a car
#     pass
# class Maruthi800(Car):
#     def break_type(self):
#         print("disc break")
# # obj=Ambassador()
# # obj.start()     
# obj=Maruthi800()
# obj.break_type()           

#
class Parent:
    props=["Passion pro","swift"]

    def get_properties(self):
        return self.props

class Child(Parent):
     def get_properties(self):
        self.p=super().get_properties()
        self.p.append("Hunter")
        return self.p

ch=Child()
print(ch.get_properties())      
              
