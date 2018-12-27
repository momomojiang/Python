class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
        
    def displayInfo(self):
        print("Price is "+self.price, "Max speed is "+self.max_speed) 
    
    def ride(self):
        print("Riding")
        self.miles+=10
        return self
    
    def reverse(self):
        print("Reversing")
        self.miles=self.miles-5
        return self




bike1=Bike("500","25mph")
bike1.displayInfo()

