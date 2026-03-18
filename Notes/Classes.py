#IC 1st class

#example one
class Animal:
    #methods
    #used common variables 
    #function used inside of it
    def __init__(self,name,species,age):
        self.name = name 
        self.species = species
        self.age = age 
    def __str__(self): 
        return(f"Name: {self.name} species: {self.species } age: {self.age}")
    def birthday(self):
        self.age += 1
    
dog = Animal("doug","dog",4)
bunny = Animal("juddy","bunny",20)
print(dog)
print(bunny)
dog.birthday()
print(dog)

#Example 2
class ClassPeriod:
    def __init__(self,subject,teacher = "Ms Larose",room = None):
        self.subject = subject.capitalize() 
        self.teacher = teacher
        self.room = room

    def __str__(self):
        return f"subject:{self.subject}\n teacher:{self.teacher}\n room{self.room}"
    
first = ClassPeriod("cp2",room = 200)
second = ClassPeriod("geography", "Dr C", room = 67,)
third = ClassPeriod("English", "Ms thornnock", room= 98)

print(first,second,third)