class Calculator:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def add(self):
        return self.num_1 + self.num_2

    def subtract(self):
        return self.num_1 - self.num_2

    def multiply(self):
        return self.num_1 * self.num_2

    def divide(self):
        if not self.num_2 == 0:
            return self.num_1 / self.num_2
        else:
            return None


if __name__ == '__main__':
    num_1 = input('Enter first number: ')
    num_2 = input('Enter second number: ')
    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
        calculator = Calculator(num_1, num_2)
        print(calculator.multiply())
    except ValueError:
        print('Invalid input')
