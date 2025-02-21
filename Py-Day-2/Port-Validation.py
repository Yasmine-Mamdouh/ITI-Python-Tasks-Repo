# Validate a Port Number

# 1) Accept a port number as input.
# 2) Check if the port number is within the valid range (0 to 65,535).
# 3) Print True if the port number is valid, otherwise print False.

port_num = input('Enter the Port Number: ')

if int(port_num) >= 0 and int(port_num) <= 65535:
    print('The port number is valid.')
else:
    print('The port number is not valid.')
