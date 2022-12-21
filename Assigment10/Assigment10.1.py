class Fractions:
    def __init__(self):
        self.numerator = 1
        self.denominator = 1
        self.sum_res = 1
        self.subtraction_res = 1
        self.multiplication_res = 1
        self.quotient_res = 1


    def sum(self, num1, num2):
        self.numerator = num1
        self.denominator = num2
        self.sum_res = num1 + num2
        return self.sum_res

    def subtraction(self, num1, num2):
        ...
        
    def multiplication(self, num1, num2):
        ...
        
    def quotient(self, num1, num2):
        ...