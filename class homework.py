class FactorialCalc:
    cache = {}

    def factorial(self):
        if self < 0:
            print("Negative factorial")
            return
        if self == 0 or self == 1:
            return 1
        if self in FactorialCalc.cache:
            return FactorialCalc.cache[self]

        FactorialCalc.cache[self] = self * FactorialCalc.factorial(self - 1)
        return FactorialCalc.cache[self]


if __name__ == '__main__':
    while True:
        try:
            user_int = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input")
            break
        else:
            print(FactorialCalc.factorial(user_int))
