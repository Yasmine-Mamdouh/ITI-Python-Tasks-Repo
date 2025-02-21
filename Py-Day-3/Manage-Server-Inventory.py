# Manage Server Inventory Using a Dictionary

# 1) Create a dictionary where:
#       Keys represent server hostnames.
#       Values represent corresponding IP addresses.
# 2) Perform the following operations on the dictionary:
#       Add a new server.
#       Update the IP address of an existing server.
#       Remove a server from the dictionary.
#       Print all servers along with their IP addresses.

servers = {
    'server1': '1.1.1.1',
    'server2': '2.2.2.2',
    'server3': '3.3.3.3'}

servers['server4'] = '4.4.4.4'      # Add
servers['server3'] = '33.33.33.33'  # Update
del servers['server1']              # Delete

print(servers)
