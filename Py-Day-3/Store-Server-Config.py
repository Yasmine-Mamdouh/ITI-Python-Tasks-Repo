# Store Immutable Server Configuration Using a Tuple

# 1) Define a tuple containing server configuration details (e.g., ("192.168.1.1", "8080", "root")).
# 2) Unpack the tuple into separate variables: IP address, port, and username.
# 3) Print the extracted configuration details.

config = ("192.168.1.1", "8080", "root")
ip, port, username = config
print(f"IP: {ip}, Port: {port}, Username: {username}")