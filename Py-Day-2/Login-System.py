# Simulate a Login System

# 1) Prompt the user to enter a username and password.
# 2) Check if:
#       The username is "admin".
#       The password is "admin123".
# 3) Print "Access granted" if both are correct; otherwise, print "Access denied".

username = input('Enter your username: ')
password = input('Enter your password: ')

if username == 'admin' and password == 'admin123':
    print('Access granted.')
else:
    print('Access denied.')
