def compare(number_1, number_2):
    if num_1 < num_2:
        return f"{num_1} is less than {num_2}"
    elif num_1 > num_2:
        return f"{num_1} is greater than {num_2}"
    elif num_1 == num_2:    # rather than "else", in case a non-number is passed
        return f"Both numbers are equal"
