# Extract Numeric Part from a Server Hostname

# 1) Accept a server hostname as input (e.g., "web-server-01").
# 2) Extract the numeric part from the string.
# 3) Convert the extracted number into an integer and print it.

server_hostname = input("Enter the Server Hostname: ")
numeric_part = server_hostname.split('-')
print(int(numeric_part[-1]))
