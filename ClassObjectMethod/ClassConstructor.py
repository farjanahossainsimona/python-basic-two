class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return 'it is imposible to divide by zero'


my_calculator = Calculator(100, 0)

temp = my_calculator.addition()
print(temp)
temp = my_calculator.subtraction()
print(temp)
temp = my_calculator.multiplication()
print(temp)
temp = my_calculator.division()
print(temp)
