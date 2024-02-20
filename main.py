def get_numbers():
    try:
        numbers = int(input("Enter valid_numbers: "))
    except ValueError:
        print("Invalid input")
    else:
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


# Like garlic bread

main()
