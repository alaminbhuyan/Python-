class employee:
    
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id
    def display(self):
        print(f'Name:{self.name}\nAge: {self.age}\nId: {self.id}')
    
    
obj = employee('alamin',21,1030)
obj.age = 40
obj.display()

print(obj.name)

del obj.age
print(employee)