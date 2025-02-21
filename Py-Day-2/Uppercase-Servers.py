# Print Server Names in Uppercase

# 1) Create a list of server names.
# 2) Iterate through the list and print each server name in uppercase.

num_servers = int(input("Enter the number of servers: "))
server_names = []

for i in range(num_servers):
    name = input(f"Enter the name of server {i+1}: ")
    server_names.append(name)

print("\nServers in Uppercase:")
for server in server_names:
    print(server.upper())
