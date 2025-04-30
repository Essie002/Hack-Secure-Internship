import socket
import sys

# Function to scan open ports
def scan_ports(ip, start_port, end_port):
    open_ports = []  # List to store open ports

    # Loop through the specified port range
    for port in range(start_port, end_port + 1):
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection

        # Try to connect to the port
        result = sock.connect_ex((ip, port))

        # If result is 0, the port is open
        if result == 0:
            open_ports.append(port)
        
        # Close the socket connection
        sock.close()

    return open_ports

# Function to handle user inputs and validate them
def main():
    # Get user input for IP, start port, and end port
    ip = input("Enter the IP address to scan: ")

    # Validate IP address format
    try:
        socket.inet_aton(ip)  # Try to convert the IP to a valid format
    except socket.error:
        print("Invalid IP address format. Exiting...")
        sys.exit(1)

    try:
        start_port = int(input("Enter the start port: "))
        end_port = int(input("Enter the end port: "))

        # Validate the port range
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("Invalid port range. Port numbers must be between 1 and 65535, and start port must not be greater than end port.")
            sys.exit(1)
    except ValueError:
        print("Invalid input for port numbers. Please enter integers.")
        sys.exit(1)

    print(f"Scanning IP address {ip} for open ports from {start_port} to {end_port}...")

    # Call the function to scan ports
    open_ports = scan_ports(ip, start_port, end_port)

    # Display the results
    if open_ports:
        print(f"Open ports on {ip}: {', '.join(map(str, open_ports))}")
    else:
        print(f"No open ports found on {ip} in the specified range.")

if __name__ == "__main__":
    main()
