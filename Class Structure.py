class Bike:
    def __init__(self,price,max_speed):
		    self.price = price
		    self.max_speed = max_speed
    def displayInfo(self):
	      print("Price is "+self.price, "Max speed is "+self.max_speed)
    def ride(self,ride_miles):
        print("Riding")
        self.miles=0
        self.miles+=int(ride_miles)
        return self
    def reverse(self,reverse_miles):
        print("Reversing")
        self.miles-=int(reverse_miles)
        return self



bike1=Bike("500","25mph")
bike1.displayInfo()

b=bike1.ride("10")
print(b)

x=bike1.reverse("5")
print(x)
