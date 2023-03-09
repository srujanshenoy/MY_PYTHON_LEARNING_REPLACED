def phone_to_text(phone_number):
    # Convert phone number to spoken format

    # Define the phone keypad dictionary
    keypad = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }

    spoken_number = ''
    prev_word = None
    count = 1

    for digit in phone_number:
        word = keypad.get(digit, '')
        if len(word) > 0:
            if word == prev_word:
                # Increment count for repeated words
                count += 1
            else:
                # Add previous word and count to spoken number
                if prev_word is not None:
                    if count > 1:
                        spoken_number += f'double {prev_word} '
                    else:
                        spoken_number += f'{prev_word} '
                # Reset count for new word
                prev_word = word
                count = 1
    # Add final word and count to spoken number
    if prev_word is not None:
        if count > 1:
            spoken_number += f'double {prev_word} '
        else:
            spoken_number += f'{prev_word} '
    return spoken_number.strip()
