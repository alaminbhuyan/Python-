class A:
    def __init__(self):
        print('hello this is parent class')

class B(A):
    def __init__(self):
        print('hello this is child class')

obj = B()