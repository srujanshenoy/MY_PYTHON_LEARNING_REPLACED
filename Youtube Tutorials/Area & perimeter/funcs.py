PI = 3.141592659


class Circle:
    def __init__(self, radius: float):
        self.area = f"The area of this circle is {PI * (radius ** 2)}"
        self.peremeter = f"The peremeter of this circle is {2 * PI * radius}"
    

class Rectangle:
    def __init__(self, side_a: float, side_b: float):
        self.area = f"The area of this rectangle is {side_a * side_b}"
        self.peremeter = f"The peremeter of this rectangle is {2 * (side_a + side_b)}"
        
        
class Square:
    def __init__(self, sidelength: float):
        self.area = f"the area of this square is {sidelength ** 2}"
        self.peremeter = f" the peremeter of this square is {sidelength * 4}"
        
        
def triangle_area(base: float, height: float):
    return f"The area of this triangle is {(0.5 * base) * height}"


def triangle_peremeter(side_a: float, side_b: float, side_c: float):
    return f"The peremeter of this triangle is {side_a + side_b + side_c}"


def continue_game():
    usr_in = input("Do you want to continue? Press enter for yes and type anything and then press enter for no. ")
    if usr_in == '':
        return True

    return False


def float_input(prompt: str):
    usr_in = "wrong"

    while True:
        usr_in = input(prompt + " ")
        try:
            return float(usr_in)

        except ValueError:
            print("NaN error")


def mode_initial():
    valid = ["1", "2", "3"]
    
    while True:
        usr_in = input(
            """
        Enter a Mode (1, 2, 3):
        1. Area
        2. Peremeter
        3. Quit
            """
        )
        
        if usr_in in valid:
            return int(usr_in)


