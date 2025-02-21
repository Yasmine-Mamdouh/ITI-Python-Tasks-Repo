# Check Server Status Using a Function

# Define a function check_server_status that:
#       Takes a server hostname as input.
#       Uses a dictionary to store server statuses (e.g., {"server1": "online", "server2": "offline"}).
#       Returns the status of the specified server.
#       Returns "Server not found" if the server does not exist.

def check_server_status(server):
    server_statuses = {
        "server1": "online",
        "server2": "offline",
        "server3": "online",
        "server4": "offline"
    }
    return server_statuses.get(server, "Server not found")


server = input('Which server do you want to check? ')
print(f"Status of {server}: {check_server_status(server)}")