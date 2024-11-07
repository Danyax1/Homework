class Rectangle:
    def __init__(self, width=0, length=0):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)


def main():
    try:
        width = float(input("Enter the width of the rectangle: "))
        length = float(input("Enter the length of the rectangle: "))
    except ValueError:
        print("Please enter an number")
    else:
        rectangle = Rectangle(width, length)
        print(f"Area: {rectangle.area()}")
        print(f"Perimeter: {rectangle.perimeter()}")


if __name__ == '__main__':
    main()
