"""
Helpers file: 
In this file there are all the function that can be used in app.py 
"""

def is_valid_input(input_text):
    # Check if the input contains only digits and spaces
    return all(char.isdigit() or char.isspace() for char in input_text)


def remove_duplicates(input_text):
    input_list = [int(x) for x in input_text.split()]
    result_list = list(set(input_list))
    return result_list
