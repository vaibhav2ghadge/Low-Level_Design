from model.rider import Rider
class RiderManger:
    def __int__(self):
        riders = {}
    
    def registerRider(self,id : int,name :str)-> None : 
        
        if id in self.riders:
            return "raise excepion"
        
        self.rider[id] = Rider(id,name)

        