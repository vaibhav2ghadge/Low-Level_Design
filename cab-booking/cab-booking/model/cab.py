

from turtle import pd


class Cab:
    def __init__(self, id, driverName):
        self.id = id
        self.driverName = driverName
        self.currentLocation = None
        self.availability = None
    
  