
class Node:
    def __init__(self,data_value=None):
        self.data_value= data_value
        self.next_value = None


obj1 = Node('Mon')
obj3 = Node('Wen')
obj2 = Node('Tue')
obj4 = Node('Thu')

obj1.next_value = obj3
obj3.next_value = obj2
obj2.next_value = obj4

value = obj1
while value:
    print(value.data_value)
    value = value.next_value
