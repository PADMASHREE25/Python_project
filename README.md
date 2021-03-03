# Python_project
In this, I have written the code for calaculator to perform basic operations like addition, subtraction,multiplication and division by using function for each operation.Based on the choice of the user the operations are performed. It will also return the result value which can be used further.
The code is as follows,

class calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def diff(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b
