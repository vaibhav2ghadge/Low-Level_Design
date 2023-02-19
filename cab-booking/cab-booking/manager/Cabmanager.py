from logging import raiseExceptions
from model.cab import Cab

class CabManager:
    def __init__(self) -> None:
        self.cabs= None
        
    def registerCab(self,id,driverName):
        
        if id in self.cabs:
            return Exception("Driver already register")
        self.cabs[id] =  Cab(id,driverName)
        
    def updateCabLocation(self,id,location):
        
        if id not in self.cabs:
            return Exception("cab not found")
        
        self.cabs[id].currentLocation = location
        
    def availibility(self,id,available):
        if id in self.cabs:
            self.cabs[id].availability = available
            return
        return Exception("cab not found")
    
        
    
        
        
        