
class Mobile:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
        self.full_name = brand+" "+model

    def display(self):
        print(f"Brand= {self.brand}\nModel= {self.model}\nPrice= {self.price}\nMobile_name= {self.full_name}")


obj = Mobile("Sumsung Galaxy","M10",13000)
# print(obj.__dict__)
obj.display()
print()
obj.price = 10500
print(obj.display())