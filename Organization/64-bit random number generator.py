import random

def gen_64(length):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890+-' # all allowed characters in the number
    out = ''
    j = 0
    while j < length:
        char = chars[random.randint(0, len(chars) - 1)]
        out += char
        j += 1

    return out

for i in range(20):
    print(gen_64(4234) + '\n')
