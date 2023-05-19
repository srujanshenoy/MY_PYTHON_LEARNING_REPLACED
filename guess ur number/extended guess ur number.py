# General format
# replace (var) with the variable name

#    (var) = input("slide (number): \n (numbers) \n")

# Verify value of (var)
# if (var) == "Y":
#    (var) = 1
# elif (var) == "N":
#    (var) = 0
# else:
#    print("Oops! This input is not valid. re-running the program")
#    continue


# after this, you have to add an STR_(var) variable where var is the name of the variable.
# before you add it to the All variable, you have to set the value to be
# str((var))
# where var is again, the name of the variable
# then add it to the All
# variable at the start of it because you are obviously going to be adding a bigger number to the program thus a
# bigger place so it has to be at the start of a binary number thus corresponding to putting it at the start.


print("choose a number from 0 - 31")
while True:
    X = input(
        """Enter a capital Y if your number appears in a slide and a capital N if not.
        enter 0 to stop.
        
slide 1:
1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31
"""
    )

    # VERIFY VALUE OF X
    if X.upper() == "Y":
        X = 1
    elif X.upper() == "N":
        X = 0
    elif X == "0":
        print("OK. We will stop. Bye Bye!")
        break
    else:
        print("Oops! This input is not valid. re-running the program")
        continue

    Y = input("slide 2: \n2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31\n")

    # Verify value of Y
    if Y.upper() == "Y":
        Y = 1
    elif Y.upper() == "N":
        Y = 0
    elif Y.upper() == "0":
        print("OK. We will stop. Bye Bye!")
        break
    else:
        print("Oops! This input is not valid. re-running the program")
        continue

    Z = input("slide 3: \n4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31\n")

    # verify value of Z
    if Z.upper() == "Y":
        Z = 1
    elif Z.upper() == "N":
        Z = 0
    elif Z.upper() == "0":
        print("OK. We will stop. Bye Bye!")
        break
    else:
        print("Oops! This input is not valid. re-running the program")
        continue

    W = input("slide 4: \n8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31\n")

    # VERIFY VALUE OF W
    if W.upper() == "Y":
        W = 1
    elif W.upper() == "N":
        W = 0
    elif W.upper() == "0":
        print("OK. We will stop. Bye Bye!")
        break
    else:
        print("Oops! This input is not valid. re-running the program")
        continue

    A = input("slide 5: \n16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31\n")
    # Verify value of a
    if A.upper() == "Y":
       A = 1
    elif A.upper() == "N":
       A = 0
    elif A.upper() == 0:
        print("OK, we will stop. Bye Bye!")
        break
        
    else:
       print("Oops! This input is not valid. re-running the program")
       continue

    # "STR" in the following is a short form for string
    STR_A = str(A)
    STR_X = str(X)
    STR_Y = str(Y)
    STR_Z = str(Z)
    STR_W = str(W)
    All = STR_A+STR_W+STR_Z+STR_Y+STR_X

    # define their value and put it in a var
    Their_Number = int(All, 2)

    # print it
    print(
        f"\n your number is {Their_Number}")
