import csv


def main():
    """Main Program"""
    countries = get_countries()
    print(MENU)
    choice = input("Enter choice: ").lower()
    while choice != "Q":
        if choice == <first option>:
            <do first task>
        elif choice == <second option>:
            <do second task>
        elif choice == <n-th option>:
            <do n-th task>
        else:
            display invalid input error message
        print(MENU)
        choice = input("Enter choice: ").lower()
    <do final thing, if needed>


def get_countries():
    pass

def print_countries():
    """Print countries"""
    pass