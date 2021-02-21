class Calculator:
    def addition(self, a, b):
        return a+b

    def subtraction(self, a, b):
        return a-b

    def multiplication(self, a, b):
        return a*b

    def division(self, a, b):
        try:
            return a/b
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'


my_calculator = Calculator()

temp = my_calculator.addition(12, 45)
print(temp)
temp = my_calculator.subtraction(50, 45)
print(temp)
temp = my_calculator.multiplication(12, 2)
print(temp)
temp = my_calculator.division(70, 0)
print(temp)
