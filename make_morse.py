
"""
Create dictionaries from morse_lib.txt, and create valid characters lists to check against
user input.
"""

with open('../../../../Downloads/morse_code-master (1)/morse_code-master/morse_lib.txt') as file:
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
LETTER_TO_MORSE_DICT[' '] = ' '

# create dictionary morse to letter with characters corresponding to values with list slices
MORSE_TO_LETTER_DICT = {}
for code in morse_data_list_format:
    MORSE_TO_LETTER_DICT[code[1:]] = code[:1]
MORSE_TO_LETTER_DICT[' '] = ' '
MORSE_TO_LETTER_DICT['?'] = ' '

# # create list of valid letters for user input
# VALID_LETTER_LIST = []
# for code in morse_data_list_format:
#     char = code[:1]
#     VALID_LETTER_LIST.append(char)
# VALID_LETTER_LIST.append('')
#
# # create list of valid morse for user input
# VALID_MORSE_LIST = []
# for code in morse_data_list_format:
#     char = code[1:]
#     VALID_MORSE_LIST.append(char)
# VALID_MORSE_LIST.append('')
# VALID_MORSE_LIST.append('?')



