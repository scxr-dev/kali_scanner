import socket
import sys
from datetime import datetime

# --- This is the new V2 script! ---

print("-" * 50)
print("Scanner V2 started at: " + str(datetime.now()))
print("-" * 50)

target = "127.0.0.1"

print("Scanning your own machine: " + target)
# The BIG change is here! We are now checking ports around 8000!
print("Checking ports from 7995 to 8005...")
print("\n")

try:
    # We changed the range to check where our server is!
    for port in range(7995, 8006):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"🎉 Wah! Found it! Port {port} is open!")
            
        s.close()

except KeyboardInterrupt:
    print("\n Aiyo! You stopped the scan.")
    sys.exit()

except socket.error:
    print("\n Wah, cannot connect to the machine. Got problem leh.")
    sys.exit()

print("\nScan finished! 🎉")

