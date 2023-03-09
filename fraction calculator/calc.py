# functions

def help():
    print(
        """
        + ==> add
        - ==> subtract
        x ==> multiply
        / ==> divide
        help ==> bring this again.
        """
    )


def two_element_list_to_f_string_and_print(list: list):
    print(f"{list[0]} / {list[1]}")


def simplify(N, D):
    hcf = compute_hcf(N, D)
    on = N / hcf
    od = D / hcf
    RESULT = [on, od]
    return RESULT


def compute_lcm(x, y):
    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm


def compute_hcf(x, y):

    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf






def multiply(N1, D1, N2, D2):
    RN = N1 * N2
    RD = D1 * D2
    if RN > RD:
        choice = input(
            "What form do you want your answer in? \n mixed fraction or improper fraction? \n type your answer to this question as specified in the question itself")
        if choice.lower() == "mixed fraction":
            Remainder = RN % RD
            Quotient = RN / RD
            Whole = int(Quotient)
            if Remainder != 0:
                RESULT = f"{Whole} {Remainder}/{RD}"
                print(RESULT)
            else:
                print(Whole)

        elif choice.lower() == "improper fraction":
            RESULT_FRACTION_LIST = [RN, RD]
            two_element_list_to_f_string_and_print(RESULT_FRACTION_LIST)

    elif RN < RD:
        print(simplify(RN, RD))

    else:
        print("1")






def divide(N1, D1, N2, D2):
    RN = N1 * D2
    RD = D1 * N2
    if RN > RD:
        choice = input(
            "What form do you want your answer in? \n mixed fraction or improper fraction? \n type your answer to this question as specified in the question itself")
        if choice.lower() == "mixed fraction":
            Remainder = RN % RD
            Quotient = RN / RD
            Whole = int(Quotient)

            RESULT = f"{Whole} {Remainder}/{RD}"
            print(RESULT)

        elif choice.lower() == "improper fraction":
            RESULT_FRACTION_LIST = [RN, RD]
            two_element_list_to_f_string_and_print(RESULT_FRACTION_LIST)

    elif RN < RD:
        print(simplify(RN, RD))

    else:
        print("1")


def add(N1, D1, N2, D2):
    LCM = compute_lcm(D1, D2)

    x_for_d1 = LCM / D1
    x_for_d2 = LCM / D2

    CN1 = N1 * x_for_d1
    CN2 = N2 * x_for_d2

    RN = CN1 + CN2
    RD = LCM
    if RN > RD:
        choice = input(
            "What form do you want your answer in? \n mixed fraction or improper fraction? \n type your answer to this question as specified in the question itself")
        if choice.lower() == "mixed fraction":
            Remainder = RN % RD
            Quotient = RN / RD
            Whole = int(Quotient)

            RESULT = f"{Whole} {Remainder}/{RD}"
            print(RESULT)

        elif choice.lower() == "improper fraction":
            RESULT_FRACTION_LIST = [RN, RD]
            two_element_list_to_f_string_and_print(RESULT_FRACTION_LIST)

    elif RN < RD:
        print(simplify(RN, RD))

    else:
        print("1")

def subtract(N1, D1, N2, D2):
    LCM = compute_lcm(D1, D2)

    x_for_d1 = LCM / D1
    x_for_d2 = LCM / D2

    CN1 = N1 * x_for_d1
    CN2 = N2 * x_for_d2

    RN = CN1 - CN2
    RD = LCM
    if RN > RD:
        choice = input(
            "What form do you want your answer in? \n mixed fraction or improper fraction? \n type your answer to this question as specified in the question itself")
        if choice.lower() == "mixed fraction":
            Remainder = RN % RD
            Quotient = RN / RD
            Whole = int(Quotient)

            RESULT = f"{Whole} {Remainder}/{RD}"
            print(RESULT)

        elif choice.lower() == "improper fraction":
            RESULT_FRACTION_LIST = [RN, RD]
            two_element_list_to_f_string_and_print(RESULT_FRACTION_LIST)

    elif RN < RD:
       print(simplify(RN, RD))

    else:
       print("1")



# end


# mainloop
while True:
    help()
    # get inputs


    N1 = int(input("numerator 1 -> "))
    D1 = int(input("denominator 1 -> "))

    if D1 == 0:
        print("invalid denominator because it is 0")
        break

    elif D1 == "help":
        help()

    elif D1 == "shud up":
        break

    OP = input("operator (+, -, x, /) -> ")

    if OP != "+" and OP != "-" and OP != "x" and OP != "/":
        print("invalid operator")
        break

    N2 = int(input("numerator 2 -> "))
    D2 = int(input("denominator 2 ->"))

    if D2 == 0:
        print("invalid denominator because it is 0")

    print(f"{N1}/{D1} {OP} {N2}/{D2}\n")

    if OP == "+":
        RESULT_LIST = add(N1, D1, N2, D2)

    elif OP == "x":
        multiply(N1, D1, N2, D2)

    elif OP == "/":
        RESULT_LIST = divide(N1, D1, N2, D2)

    elif OP == "-":
        subtract(N1, D1, N2, D2)

    elif OP == "shud up":
        break
