import re

# def fizzBuzz(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return 'FizzBuzz'
#
#     elif n % 3 == 0:
#         return 'Fizz'
#
#     elif n % 5 == 0:
#         return 'Buzz'
#     else:
#         return n
#
#
# for n in range(1, 20):
#     print(fizzBuzz(n))
password = input("Input your password: ")


def validate_password(passwords):
    while passwords:
        # Check if the password has at least 8 characters
        if len(passwords) < 8:
            return print("The password is weak")
        # Check if the password contains at least one special character
        if re.search(r'[!@#$%^&*(),.?":{}|<>0-9]', passwords):
            return print("The password is strong")

        # Check if the password contains at least one uppercase lowercase letter
        if not re.search(r'[A-Z,a-z]', passwords):
            return False
        else:
            return print("The password is medium/strong")
    return True


is_valid = validate_password(password)

if is_valid:
    print("Valid Password.")
else:
    print("Password does not meet requirements.")

    # If all the conditions are met, the password is valid
    # return True

    # # Check if the password contains at least one lowercase letter
    # if not re.search(r'[A-Z,a-z]', password):
    #     return False
    # else:
    #     return print("The password is medium/strong")

    # Check if the password contains at least one digit
    # if re.search(r'\d', password):
    #     return False
