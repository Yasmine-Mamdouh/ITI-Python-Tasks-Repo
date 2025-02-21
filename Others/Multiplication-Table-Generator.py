# Multiplication Table Generator

# Write a program that generates a multiplication table from 1 to the given number.
# 1) Accept an integer input from the user.
# 2) Construct the table as a list of lists, where:
#       The first list contains the multiples of 1.
#       The second list contains the multiples of 2.
#       The third list contains the multiples of 3, and so on.
# => Example:
#       If the input is 3, the output should be: [[1], [2, 4], [3, 6, 9]].
#       Print the generated multiplication table.

def multip_table(n):
    table = []
    i = 1
    while i <= int(n):
        j = 1
        num = []
        while j <= i:
            num.append(i*j)
            j += 1
        table.append(num)
        i += 1
    return table


number = input('Enter the passed number: ')
print(multip_table(number))
