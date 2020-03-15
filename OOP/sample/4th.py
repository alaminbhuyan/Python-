class parent:
    def __init__(self):
        print('hello this is parent class')

class child(parent):
    def __init__(self):
        print('hello this is child class')
        super().__init__()
        


obj=child()
