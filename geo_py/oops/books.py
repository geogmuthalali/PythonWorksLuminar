class Book:
    book_name:str
    author:str
    price:int
    pages:int
#           ->__init__ 
    def __init__(self,book_name,author,price,pages):
        self.book_name=book_name
        self.author=author
        self.price=price
        self.pages=pages
        # initialising instance variable constructor()

    def get(self):
        print(self.book_name,self.price)

    def __str__(self):
        return self.book_name+str(self.price)    
       

obj=Book("one-piece vol-one","oda",499,250)
print(obj)
print(obj.book_name)
obj2=Book("Naruto vol-one","kishimotto",599,30)
print(obj2.author)
# print(obj.self)