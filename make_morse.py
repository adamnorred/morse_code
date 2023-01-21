
"""
Create dictionaries from morse_lib.txt, and create valid characters lists to check against
user input.
"""

with open('morse_lib.txt') as file:
    morse_data_list = file.readlines()

morse_data_list_format = []

# clear list from \t char
for item in morse_data_list:
    f_string = item.replace('\t', '')
    morse_data_list_format.append(f_string)

morse_data_list = morse_data_list_format.copy()  # copy updated list into main list
morse_data_list_format.clear()  # clear formatted list so it can be used again

# clear list from \n char
for item in morse_data_list:
    f_string = item.replace('\n', '')
    morse_data_list_format.append(f_string)

# create dictionary letter to morse with characters corresponding to values with list slices
LETTER_TO_MORSE_DICT = {}
for code in morse_data_list_format:
    LETTER_TO_MORSE_DICT[code[:1]] = code[1:]
LETTER_TO_MORSE_DICT[' '] = '?'  # needed for formatting morse into readable message

# create dictionary morse to letter with characters corresponding to values with list slices
MORSE_TO_LETTER_DICT = {}
for code in morse_data_list_format:
    MORSE_TO_LETTER_DICT[code[1:]] = code[:1]
# needed for formatting morse into readable message
MORSE_TO_LETTER_DICT[' '] = ' '
MORSE_TO_LETTER_DICT['?'] = ' '
