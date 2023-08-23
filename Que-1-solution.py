import re

def is_valid_contact_number(number):
    # Defining the regular expression pattern for valid of contact numbers
    pattern = r'^(\+?\d{0,2})?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{2,5}[-.\s]?\d{2,5}$'
    
    # Checking if the number matches the pattern
    if re.match(pattern, number): #
        return True
    else:
        return False

# Test cases
contact_numbers = [
    "2124567890",
    "212-456-7890",
    "(212)456-7890",
    "(212)-456-7890",
    "212.456.7890",
    "212 456 7890",
    "+12124567890",
    "+1 212.456.7890",
    "+212-456-7890",
    "1-212-456-7890",
    "2323-2334-3343",
    "+91+7309987978"
]

for number in contact_numbers:
    if is_valid_contact_number(number):
        print(f"{number} is a valid contact number.")
    else:
        print(f"{number} is an invalid contact number.")
