def remove_duplicates(input_text):
    input_list = [int(x) for x in input_text.split()]
    result_list = list(set(input_list))
    return result_list
