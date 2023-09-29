def is_valid_input(input_text):
    # Check if the input contains only digits and spaces
    return all(char.isdigit() or char.isspace() for char in input_text)


def remove_duplicates(input_text):
    input_list = [int(x) for x in input_text.split()]
    result_list = list(set(input_list))
    return result_list

def test_valid_input():
    input_text = "123, 456, 789"
    assert not is_valid_input(input_text)

def test_invalid_input():
    input_text = "123, ABC, 789"
    assert not is_valid_input(input_text)

def test_remove_duplicates():
    input_text = "1 2 3 2 4 5 6 5"
    result = remove_duplicates(input_text)
    assert result == [1, 2, 3, 4, 5, 6]

def test_performance():
    input_text = "1 " * 1000000  # Simulate a large input
    result = remove_duplicates(input_text)
    assert len(result) == 1  # Assuming duplicates are removed