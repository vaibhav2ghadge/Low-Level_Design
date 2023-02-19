import math
class Location:
    def __init__(self,x1,y1) -> None:
        self.x1 =x1
        self.y1 = y1
        
    def getDistance(self):
        return math.sqrt((self.x1-self.x2)**2 +
                         (self.y1-self.y2)**2)
    
        
    
    
    
    