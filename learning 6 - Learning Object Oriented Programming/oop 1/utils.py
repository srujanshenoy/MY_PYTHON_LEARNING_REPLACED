class Math:
    def __init__(self, numbers: list):
        self.numbers = numbers

    def ascending(self):
        sequence = self.numbers

        for i in range(1, len(sequence)):
            key = sequence[i]  # current value
            j = i - 1  # previous index

            while j >= 0 and sequence[j] > key:
                # when j is a positive number, and the previous value is greater than the current value:

                sequence[j + 1] = sequence[j]
                #        ^^^^^         ^^^^
                #      current index   previous index

                # So this means we are saying that the current index is now the previous index
                j -= 1
                # we have to decrement j to continue searching through the sequence.

            sequence[j + 1] = key
            # this inserts the value the same position as we need as
            # j is defined as  i - 1, and we are doing j + 1
            # the +1 & -1 cancel each other, so we end up inserting at the exact index
        return sequence

    def descending(self):
        sequence = self.numbers

        for i in range(1, len(sequence)):
            key = sequence[i]  # current value
            j = i - 1  # previous index

            while j >= 0 and sequence[j] < key:
                # when j is a positive number, and the previous value is less than the current value:

                sequence[j + 1] = sequence[j]
                #        ^^^^^         ^^^^
                #      current index   previous index

                # So this means we are saying that the current index is now the previous index
                j -= 1
                # we have to decrement j to continue searching through the sequence.

            sequence[j + 1] = key
            # this inserts the value the same position as we need as
            # j is defined as  i - 1, and we are doing j + 1
            # the +1 & -1 cancel each other, so we end up inserting at the exact index
        return sequence

    # class Area:
    #     def __init__(self, length:float, breadth:float, height:float, radius:float, side:float):
    #         self.length = length
    #         self.breadth = breadth
    #         self.height = height
    #         self.radius = radius
    #         self.side = side
    #
    #     def rectangle(self):
    #         l = self.length
    #         b = self.breadth
    #         return l*b
    #
    #     def square(self):
    #         a = self.side
    #         return a**2
    #
    #     def triangle(self):
    #         h = self.height
    #         b = self.breadth
    #         return 1/2 * h * b

    class Geometry:
        class Square:
            def __init__(self, a: float):
                self.a = a

            def area(self):
                return self.a ** 2

            def perimeter(self):
                return self.a * 4

        class Rectangle:
            def __init__(self, length: float, breadth: float):
                self.length = length
                self.breadth = breadth

            def area(self):
                return self.length * self.breadth

            def perimeter(self):
                return 2 * (self.length + self.breadth)

        class Circle:
            def __init__(self, radius: float):
                self.radius = radius

            def area(self):
                return 3.141592659 * self.radius ** 2

            def perimeter(self):
                return 2 * 3.141592659 * self.radius

        class Triangle:
            def __init__(self, height: float, breadth: float, S1: float, S2: float, S3: float):
                self.height = height
                self.breadth = breadth
                self.S1 = S1
                self.S2 = S2
                self.S3 = S3

            def area(self):
                return 1 / 2 * self.height * self.breadth

            def perimeter(self):
                return self.S1 + self.S2 + self.S3


def select():
    selection = input(("""
    1. Ascending order
    2. Descending order
    3. Square Area
    4. Square Perimeter
    5. Rectangle area
    6. Rectangle Perimeter
    7. Triangle area
    8. Triangle Perimeter
    9. Circle Area
    10. Circle Perimeter (Circumference)
    11. stop 
    """))

    try:
        selection = int(selection)
    except:
        print("not a number,")

    valid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    if selection not in valid:
        print("invalid selection.")
        select()

    elif selection in valid:
        return selection

    else:
        print("somthing went wrong...")


def check_float(value):
    while True:
        entered = input(f"{value}: ")
        try:
            value = float(entered)
            break
        except:
            print("Not a number")

    return value



