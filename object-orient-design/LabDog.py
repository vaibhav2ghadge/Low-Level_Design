from dog import Dog

class Labdog(Dog):
        def __init__(self, name: str,
                     age: int,) -> None:
            super().__init__(name, age)
            
        def speed(self) -> None:
            print("WOW")
            

labdog = Labdog("Nancy",12)
print(labdog.getName())
print(labdog.speed())
            