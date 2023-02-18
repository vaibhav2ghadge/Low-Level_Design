import threading

class Singleton:
    # this is static variable it can be accesable by any class
    _instance = None
    _lock = threading.Lock()

    # its get called before the __init__
    # we can do some stuff before and after object creation
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)

            return cls._instance


s1 = Singleton()
s2 = Singleton()
print(s1 is s2) # True
print(s1) # <__main__.Singleton object at 0x106fc9110>
print(s2) # <__main__.Singleton object at 0x106fc9110>
