# Code Explainations

## Funcs.py

### Float input

```py
def float_input(prompt: str):
    """
    :param prompt: prompt for floating point input
    :return: float
    """
    usr_in = "wrong"

    while True:
        usr_in = input(prompt + " ")
        try:
            return float(usr_in)

        except ValueError:
            print("NaN error")
```

Float input is a function that gives a prompt specified by the programmer (`prompt: str`) to the User and returns a floating-point value.
In the while true loop, the programmer's prompt if given to the user. It will be checked if it can be converted into a floating point number, if not, it repeats, asking the user again.

### Programme Mode

```python
def programme_mode():
    usr_in = "wrong"

    while True:
        usr_in = input("""
        Enter a mode, 1 or 2.

        1. x% of y = __
        2. x is __% of y
        3. Quit
        """)

        if usr_in in ["1", "2", "3"]:
            return int(usr_in)
```

Programme mode is a function that prompts the user to input a number 1, 2, or 3 to either do function 1, 2, or 3. If the user's input is not in 1, 2, or 3, it repeats the same question.

## Main.py

1st, it checks the mode that the user wants to use the programme in (This is all contained in a while true loop for easy looping).
==> ```mode = programme_mode```

### Mode 1: x% of y is __

Formula:
