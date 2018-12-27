class Product:
	def __init__(self,price,item_name,weight,brand):
		self.price=price
		self.itme_name=item_name
		self.weight=weight
		self.brand=brand
		self.status="for sale"
		self.tax=1.15

	def sell(self):
		self.status="sold"
	def add_tax(self):
		self.price+=self.price*self.tax
		return self.price
	def return_item(self,reason_for_return):
		if reason_for_return == "defective":
		    self.status = "defective"
		    self.price = 0
		    return self.status,self.price
		if reason_for_return == "like new":
		    self.status = "like new"
		    self.price = self.price
		    return self.status,self.price
		if reason_for_return == "opened":
		    self.status = "used"
		    self.price = self.price*0.8
			
		    return self.status,self.price





product1=Product(0.99,"apple","5oz","Fuji")
product1.sell()
print(product1.status)

x=product1.add_tax()
print(x)

z=product1.return_item("like new")
print(z)



