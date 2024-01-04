import socket
import threading

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address (host and port)
server_host = '127.0.0.1'  # Change this to the server's IP address
server_port = 12345

# Connect to the server
client_socket.connect((server_host, server_port))

# Send the client's name to the server
name = 'E'
client_socket.send(name.encode('utf-8'))


def receive_messages():
    while True:
        try:
            # Receive messages from the server
            response = client_socket.recv(1024).decode('utf-8')
            print(f'Received from server: {response}')
        except Exception as e:
            print(f"Error receiving message: {e}")
            break


# Create a thread to continuously receive messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True  # This will allow the thread to exit when the main program exits
receive_thread.start()

while True:
    # Send a message to the server or another client
    recipient = input("Enter recipient (client name or 'all'): ")
    message = input("Enter your message: ")
    data = f"{recipient}:{message}"
    client_socket.send(data.encode('utf-8'))

    # Wait for acknowledgment from the server
    acknowledgment = client_socket.recv(1024).decode('utf-8')
    print(f'Received acknowledgment from server: {acknowledgment}')
