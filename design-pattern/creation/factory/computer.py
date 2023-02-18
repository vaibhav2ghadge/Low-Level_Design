
from abc import ABC,abstractmethod

class Computer(ABC):
  
  @abstractmethod
  def getRam(self):
      pass
  
  @abstractmethod
  def getStorage(self):
      pass
  
  @abstractmethod
  def getCpu(self):
      pass
  
  
class Server(Computer):
    def __init__(self,ram,storage,cpu) -> None:
        self.ram = ram
        self.cpu = cpu
        self.storage = storage
        
    def getRam(self):
        return self.ram
    
    def getStorage(self):
        return self.storage
    
    def getCpu(self):
        return self.cpu
    
    
class PC(Computer):
    def __init__(self,ram,storage,cpu) -> None:
        self.ram = ram
        self.cpu = cpu
        self.storage = storage
        
    def getRam(self):
        return self.ram
    
    def getStorage(self):
        return self.storage
    
    def getCpu(self):
        return self.cpu
        
        
class ComputerFactory():
    @staticmethod
    def getComputer(type,ram,storage,cpu):
        if type=="PC":
            return PC(ram,storage,cpu)
        elif type=='SERVER':
            return Server(ram,storage,cpu)
        return None


if __name__ == "__main__":
    server = ComputerFactory.getComputer("SERVER",12,500,2)
    print(server.getRam())