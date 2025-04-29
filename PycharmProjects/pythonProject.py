
class Calculator:
    # Constructor
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
        print(f"Calculator initialized with numbers: {self.num1} and {self.num2}")

    def add(self):
        return self.num1 + self.num2

    def multiply(self):
        return self.num1 * self.num2

# Creating an object (constructor is called here)
calc = Calculator(10, 5)

# Using methods
print("Addition:", calc.add())
print("Multiplication:", calc.multiply())
