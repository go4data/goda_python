# Create a sample server.log file for testing
sample_logs = [
    "[2024-07-21 10:15:32] ERROR: Database connection failed",
    "[2024-07-21 10:16:11] INFO: User 'admin' logged in", 
    "[2024-07-21 10:17:45] WARNING: Disk usage above 80%",
    "[2024-07-21 10:18:22] ERROR: Timeout occurred",
    "[2024-07-21 10:19:05] INFO: Backup completed successfully",
    "[2024-07-21 10:20:33] WARNING: Memory usage high",
    "[2024-07-21 10:21:17] INFO: System reboot initiated",
    "[2024-07-21 10:22:44] ERROR: Permission denied",
]

with open("server.log", "w") as f:
    for log in sample_logs:
        f.write(log + "\n")

print("Sample server.log file created!")