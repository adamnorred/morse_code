from make_morse import LETTER_TO_MORSE_DICT, MORSE_TO_LETTER_DICT


# user choice for encode or decode
while True:
    user_input_choice = input('Type "e" to encode, or "d" for decode: ').lower()
    if user_input_choice != 'e' and user_input_choice != 'd':
        print('Wrong input. Try again.')
        continue
    else:
        break

# check if user input is valid and there are no spelling mistakes
is_on = True
while is_on:
    if user_input_choice == 'e':
        user_input_text = input('Enter text to encode: ').upper()
    else:
        user_input_text = input('Enter text to decode(use "?" for whitespace for better formatting): ').upper()
        user_input_text = user_input_text.split()

    if user_input_choice == 'e':
        for ch in user_input_text:
            if ch in LETTER_TO_MORSE_DICT.keys():
                is_on = False  # after for loop ends, while loop ends, because there are no spelling mistakes
                continue
            else:
                is_on = True
                print('Invalid characters. Only A-Z, 0-9 and whitespaces. Try again.')
                break
    else:
        for code in user_input_text:
            if code in MORSE_TO_LETTER_DICT.keys():
                is_on = False  # after for loop ends, while loop ends, because there are no spelling mistakes
                continue
            else:
                is_on = True
                print('Invalid characters. Check your code formatting. Try again.')
                break

# makes translated message
translated_message = ''
if user_input_choice == 'e':
    for ch in user_input_text:
        translated_message += LETTER_TO_MORSE_DICT[ch] + ' '
    print(f'Encoded message: {translated_message}')

else:
    for code in user_input_text:
        translated_message += MORSE_TO_LETTER_DICT[code]
    print(f'Decoded message: {translated_message}')
