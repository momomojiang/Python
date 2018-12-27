class Car:
    def __init__(self,price,speed,fuel,mileage,tax):
        self.price=price
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
        if self.price>"10000":
            self.tax="0.15"
        else:
            self.tax="0.12"
    
    def display_all(self):
        print("The price is "+self.price+"\n")
        print("The speed is "+self.speed)
        print("The fuel is "+self.fuel)
        print("The mileage is "+self.mileage)
        print("Tax is " +self.tax)
          

car1=Car("15000","80mph","Full","3000","15000")
car2=Car("10000","80mph","Full","3000","10000")
car3=Car("18000","80mph","Full","3000","18000")
car4=Car("9000","80mph","Full","3000","9000")
car5=Car("18000","80mph","Full","3000","18000")
car6=Car("9000","80mph","Full","3000","9000")
car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()
