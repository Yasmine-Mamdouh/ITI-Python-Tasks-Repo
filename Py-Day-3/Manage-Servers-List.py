# Manage a List of Servers

# 1) Create a list of server hostnames (e.g., ["server1", "server2", "server3"]).
# 2) Perform the following operations on the list:
#       Add a new server.
#       Remove an existing server.
#       Check if a specific server exists in the list.
#       Print all servers in the list.

servers = ["server1", "server2", "server3"]
servers.append('server4')
servers.remove('server1')

server = input('Which server do you want to check? ')

if server in servers:
    print('The server exists in the list')
else:
    print('The server doesnot exist in the list')

print(servers)
          
