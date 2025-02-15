""" Strings (str)
Write a program that receives a string from the user and converts it to uppercase.
"""
def to_uppercase(word):
    uppercase_word = word.upper()
    return uppercase_word

#uppercase_word = to_uppercase(input('Enter your name: '))

""" Create a program that receives the user's full name and prints the name with all letters in lowercase."""
def to_lowercase(full_name):
    lowercase_name = full_name.lower()
    return lowercase_name

#lowercase_name = to_lowercase(input('Enter your full name: '))

""" Develop a program that asks the user to enter a phrase and then prints the phrase without leading or trailing spaces."""
def remove_whitespace_start_end(phrase):
    cleaned_phrase = phrase.strip()
    return cleaned_phrase

#cleaned_phrase = remove_whitespace_start_end(input('Enter your phrase: '))

""" Write a program that asks the user to type a date in the format "dd/mm/yyyy" and then prints the day, month, and year separately."""

def separate_day_month_year(informed_date):
    date_dict = {
        'day' : informed_date[0:2],
        'month' : informed_date[3:5],
        'year' : informed_date[6:10]
    }
    return date_dict

#date_dict = separate_day_month_year(input('Enter the date: '))
#day = date_dict['day']
#month = date_dict['month']
#year = date_dict['year']

#print(f'The day entered was {day}')
#print(f'The month entered was {month}')
#print(f'The year entered was {year}')

""" Write a program that concatenates two strings provided by the user."""

def concatenate_strings(string1, string2):
    strings_list = [
        string1, 
        string2
    ]
    concatenated_string = "".join(strings_list)
    return concatenated_string

#concatenated_string = concatenate_strings(input('Enter the first string: '), 
#                                           input('Enter the second string: '))


""" Booleans (bool)"""
""" Develop a program that asks the user to enter a boolean value and then inverts that value."""

def invert_bool(input_value: bool):
    processed_input = input_value.strip().lower()
    if processed_input in ['true', 1]:
        return False
    elif processed_input in ['false', 0]:
        return True

#inverted_boolean = invert_bool(input('Enter True or False: '))

""" Write a program that compares if two numbers provided by the user are equal."""

def compare_2_values(num1, num2):
    if num1 == num2:
        identical_flag = True
    else:
        identical_flag = False
    return identical_flag

#numbers_are_equal = compare_2_values(input('Enter the first number: '),
#                                      input('Enter the second number: '))
