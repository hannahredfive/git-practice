def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    counter = 0
    for number in numbers:
        if number > counter:
            counter = number
    
    for number in numbers:
        if number == counter:
            return number


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
