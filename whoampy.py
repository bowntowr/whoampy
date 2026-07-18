# github.com/bowntowr/whoampy
# I'm a beginner, so my code might not be the best, but I hope it works!
# I promise these comments were made by me and not AI, I just leave a lot of comments :D

# importing da stuff
import socket

# getting hostname and ip with socket and assigning to variables
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# printing the hostname and ip address to show the user
print("Hostname: ", hostname)
print("IP Address: ", ip_address)

# print a little divider
print("─" * 10)

# keep terminal open after run
input("Press Enter to exit...")