from utils import Math
import utils


while True:
    selection = utils.select()
    if selection == 1:  # ascending order
        unsorted_list = []
        print("Keep typing numbers until you want to stop, then just type anything else.")
        while True:
            appending_num = input("-> ")
            try:
                appending_num = float(appending_num)
            except:
                pass
            if type(appending_num) != float:
                break
            if type(appending_num) == float:
                unsorted_list.append(appending_num)
        print(Math.ascending(Math(unsorted_list)))

    elif selection == 2:  # ascending order
        unsorted_list = []
        print("Keep typing numbers until you want to stop, then just type anything else.")
        while True:
            appending_num = input("-> ")
            try:
                appending_num = float(appending_num)
            except:
                pass
            if type(appending_num) != float:
                break
            if type(appending_num) == float:
                unsorted_list.append(appending_num)
        print(Math.descending(Math(unsorted_list)))

    # IMPORTANT NOTE
    # FOR CASE 1 & 2:
    # THERE IS A FUNCTION IN UTILS TO DO THIS, BUT IT IS FOR OTHER FUNCTIONS.
    # AS THIS IS FOR ENTERING, THE SAME FUNCTION WILL NOT WORK.

    elif selection == 3:  # square area
        a = utils.check_float("side-length")
        a = Math.Geometry.Square(a)
        print(a.Math.Geometry.Square.area())

    elif selection == 4:  # square perimeter
        a = utils.check_float("side-length")
        a = Math.Geometry.Square(a)
        print(a.Math.Geometry.Square.perimeter())

    elif selection == 5:  # rectangle area
        l = utils.check_float("length")
        b = utils.check_float("breadth")
        print(Math.Geometry.Rectangle.area(Math.Geometry.Rectangle(l, b)))

    elif selection == 6:  # rectangle perimeter
        l = utils.check_float("length")
        b = utils.check_float("breadth")
        print(Math.Geometry.Rectangle.perimeter(Math.Geometry.Rectangle(l, b)))

    elif selection == 7: #  triangle area
        h = utils.check_float("height")
        b = utils.check_float("breadth")
        print(Math.Geometry.Triangle.area(Math.Geometry.Triangle(h, b, 0, 0, 0)))

    elif selection == 8:  # triangle perimeter
        S1 = utils.check_float("Side 1")
        S2 = utils.check_float("Side 2")
        S3 = utils.check_float("Side 3")
        print(Math.Geometry.Triangle.perimeter(Math.Geometry.Triangle(0, 0, S1, S2, S3)))

    elif selection == 9: # circle area
        r = utils.check_float("Radius")
        print(Math.Geometry.Circle.area(Math.Geometry.Circle(r)))

    elif selection == 10: # circle perimeter(Circumference)
        r = utils.check_float("Radius")
        print(Math.Geometry.Circle.perimeter(Math.Geometry.Circle(r)))

    else:
        print("We dont know what happened, please close the console or terminal and restart the app.")
        print("If you had typed 11, We will stop the program for you.")
        break





