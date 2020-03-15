class Area:
    def __init__(self):
        self.dim1 = int(input('Enter the first value: '))
        self.dim2 = int(input('Enter the second value: '))
    def area(self):
        print('The area function')

class rectangle(Area):
    def area(self):
        result= self.dim1 * self.dim2
        print('The Rectangle area is : ',result)

class triangle(Area):
    def area(self):
        result = 0.5 * self.dim1 * self.dim2
        print('The triangle area is: ',result)


obj = rectangle()
obj.area()
obj2 = triangle()
obj2.area()