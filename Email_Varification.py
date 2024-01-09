# a-z      ishita@gmail.com
# 0-9
# @ . _ times 1
# . position 3,4
# The email address should start with one or more lowercase letters (a-z).
# It can contain an optional dot (.) or underscore (_) after the first lowercase letter.
# It should contain the "@" symbol.
# The domain part should consist of alphanumeric characters (\w) and may contain multiple subdomains separated by dots.
# The top-level domain (TLD) should consist of 2 to 3 lowercase letters (e.g., "com" or "org").


# Define the regular expression pattern for password validation
    # Password should have:
    # - At least 8 characters
    # - At least one uppercase letter
    # - At least one lowercase letter
    # - At least one digit
    # - At least one special character (e.g., !@#$%^&*)


def is_valid_email(email):
    # Check if the length of the email is at least 6 characters
    if len(email) < 6:
        return 'Email is not valid 1'
    
    # Check if the first character is an alphabet
    if not email[0].isalpha():
        return 'Email is not valid 2'

    # Check if there's exactly one "@" symbol in the email
    if email.count('@') != 1:
        return 'Email is not valid 3'

    # Check for valid domain extensions (.com or .in)
    if not (email.endswith('.com') or email.endswith('.in')):
        return 'Email is not valid 4'

    # Check for invalid characters and white spaces
    for char in email:
        if char.isspace():
            return 'Email is not valid 5'
        elif char.isupper():
            return 'Email is not valid 5'
        elif char not in ['_', '.', '@'] and not char.isalnum():
            return 'Email is not valid 5'

    return 'Valid Email'

def is_valid_password(password):
    # Check if the length of the password is at least 8 characters
    if len(password) < 8:
        return 'Invalid Password 1'

    # Check if the password meets the required criteria
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in '!@#$%^&*' for char in password)

    if not (has_uppercase and has_lowercase and has_digit and has_special):
        return 'Invalid Password 2'

    return 'Valid Password'

user_email = input('Enter your Email: ')
email_result = is_valid_email(user_email)
print(email_result)

if email_result == 'Valid Email':
    user_password = input('Enter the Password: ')
    password_result = is_valid_password(user_password)
    print(password_result)


