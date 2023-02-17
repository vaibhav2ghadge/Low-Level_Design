

import string


class Dog:
    def __init__(self,name:string,age:int) -> None:
        self.name = name
        self.age = age
    
    def getName(self) -> string:
        return f"my name is {self.name}"
    
    def __str__(self) -> str:
        return f"this is string of dog object {self.name} and age {self.age}"

dog = Dog("moti",12)
print(dog.name)        
print(dog.getName())
print(dog)