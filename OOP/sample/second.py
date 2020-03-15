class A:
    section = 47
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        #print(self.name,self.age,A.section)
        print(self.name,self.age,self.section)
   

obj = A('alamin', 21)
obj.display()

obj2 = A('Tania',21)
obj2.display()

