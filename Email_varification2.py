# a-z      ishita@gmail.com
# 0-9
# @ . _ times 1
# . position 3,4
# The email address should start with one or more lowercase letters (a-z).
# It can contain an optional dot (.) or underscore (_) after the first lowercase letter.
# It should contain the "@" symbol.
# The domain part should consist of alphanumeric characters (\w) and may contain multiple subdomains separated by dots.
# The top-level domain (TLD) should consist of 2 to 3 lowercase letters (e.g., "com" or "org").

import re  # Import RegX module
def is_valid_email(email):
    

    email_condition = '^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'

    if re.search(email_condition,user_email) and ' ' not in user_email:
        return True
    else:
        return False

# Define the regular expression pattern for password validation
    # Password should have:
    # - At least 8 characters
    # - At least one uppercase letter
    # - At least one lowercase letter
    # - At least one digit
    # - At least one special character (e.g., !@#$%^&*)
def is_valid_password(password):
    
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

    # Use re.match to check if the password matches the pattern
    if re.match(pattern, password):
        return True
    else:
        return False



# Input an Email from the user
user_email = input('Enter your Email : ')

# Check if the entered Email is valid
if is_valid_email(user_email):
    print('Valid Email')
    # Input a password from the user
    user_password = input("Enter a password: ")

    # Check if the entered password is valid
    if is_valid_password(user_password):
        print("Valid Password")
    else:
        print("Invalid Password") 
else:
    print('Invalid Email') 

  

# EXPLAINATION:

# email_condition = '^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'

# ^[a-z]+: The email address should start with one or more lowercase letters (a-z).
# [\._]?: It can contain an optional dot (.) or underscore (_) after the first lowercase letter.
# [a-z0-9]+: This matches one or more lowercase letters or digits after the dot or underscore.
# @: It should contain the "@" symbol.
# [\w]+: The domain part should consist of alphanumeric characters (\w), which matches one or more characters.
# \.: Matches a dot (.) to separate the domain from the top-level domain.
# [a-z]{2,3}$: The top-level domain (TLD) should consist of 2 to 3 lowercase letters (e.g., "com" or "org").
# $: This anchors the regex to the end of the string, ensuring that there are no extra characters after the email address. 
 

# pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$" 

# (?=.*[A-Z]): At least one uppercase letter (A-Z) must be present in the password.
# (?=.*[a-z]): At least one lowercase letter (a-z) must be present in the password.
# (?=.*\d): At least one digit (0-9) must be present in the password.
# (?=.*[@$!%*?&]): At least one special character from the set @$!%*?& must be present in the password.
# [A-Za-z\d@$!%*?&]{8,}: The password must consist of characters from the set [A-Za-z\d@$!%*?&] and have a minimum length of 8 characters.
# Here's a detailed breakdown of each part of the regular expression:

# ^: Anchors the regex to the start of the string, ensuring that the password starts with the specified criteria.
# (?=.*[A-Z]): Positive lookahead assertion for an uppercase letter.
# (?=.*[a-z]): Positive lookahead assertion for a lowercase letter.
# (?=.*\d): Positive lookahead assertion for a digit.
# (?=.*[@$!%*?&]): Positive lookahead assertion for at least one special character.
# [A-Za-z\d@$!%*?&]{8,}: Matches characters from the specified set [A-Za-z\d@$!%*?&] for a minimum length of 8 characters.
# $: Anchors the regex to the end of the string, ensuring that the password meets all the criteria without extra characters.  