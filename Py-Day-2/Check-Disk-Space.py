# Check Available Disk Space

# 1) Prompt the user to enter the available disk space as a percentage.
# 2) Display the appropriate message based on the following conditions:
#       If disk space is less than 10%, print "Warning: Low disk space!".
#       If disk space is between 10% and 20%, print "Warning: Disk space is getting low.".
# 3) Otherwise, print "Disk space is sufficient.".

# tds => Total Disk Size
# ads => Available Disk Size
tds = eval(input('Enter the total disk size: '))
ads = eval(input('Enter the available disk size: '))

if ads < (tds*0.1):
    print('Warning: Low disk space!')
elif ads > (tds*0.1) and ads < (tds*0.2):
    print('Warning: Disk space is getting low.')
else:
    print('Disk space is sufficient.')
