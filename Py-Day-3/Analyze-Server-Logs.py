# Analyze Server Logs Stored as Tuples

# 1) Create a list of tuples where each tuple represents a log entry (e.g., ("server1", "error", "2023-10-01")).
# 2) Perform the following log analysis tasks:
#       Count the number of error logs.
#       Extract all log entries for a specific server.

servers_log = [
    ("server1", "error", "2023-10-01"),
    ("server2", "sshd", "2023-10-02"),
    ("server3", "login", "2023-10-03"),
    ("server1", "login", "2023-10-04"),
]

error_count = 0
for log in servers_log:
    if log[1] == 'error':
        error_count += 1
print(error_count)

for server in servers_log:
    if server[0] == 'server1':
        print(server)
