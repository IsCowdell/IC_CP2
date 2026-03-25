#Example of inheritance 


#inheritance "is a "

#Parent class
class Vehical:
    def __init__(self,model,brand):
        self.brand = brand
        self.model = model 
    def move(self):
        print("Move!")


#child class

class Car(Vehical):
    pass


class Boat(Vehical):
    def move(self):
        print("Sail!")

class Plane(Vehical):
    def move(self):
        print("fly")


car = Car("ford","mustang")
boat = Boat("ibizA","MEIC")
plane = Plane("boeing","373")

print(boat.brand)
print(boat.model)

print(car.brand)
print(car.model)
 
boat.move()
plane.move()



#aggreagation "Has a"

class Library:
    def __init__(self,name,catalog = []):
        self.name = name
        self.catalog = catalog

    def add_book(self,book):
        self.catalog.append(book)

    def remove_book(self,book):
        if book in self.catalog:
            self.catalog.pop(book)
        else:
            print("that book isn't in the library")

    def view_catolog(self):
        for book in self.catalog:
            print(book)
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"
    

lib = Library("Provo Library")


lib.add_book(Book{"way of kind""brandon sanderson"})