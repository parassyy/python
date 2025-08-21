class calculator:
    def __init__(self,v1, v2):   #constructor
        self.v1 = v1
        self.v2 = v2
    def add(self):  #instance method
        print(f'The sum of {self.v1} and {self.v2} is: {self.v1 + self.v2}')
    def subtract(self): #instance method
        print(f'The difference of {self.v1} and {self.v2} is: {self.v1 - self.v2}')
calc = calculator(1, 5)
calc.add()  
calc.subtract()
        