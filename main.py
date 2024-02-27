def get_numbers():
    """Function gets number"""
    text = input("Enter numbers separated by commas: ")
    values = text.split(' , ')
    numbers = [float(value) for value in values]
    return numbers


def square_numbers(numbers):
    pass


def display_numbers(numbers):
    """ display numbers """
    pass


def main():
    numbers = get_numbers()
    square_numbers(numbers)
    display_numbers(numbers)


# I Like garlic bread

main()
