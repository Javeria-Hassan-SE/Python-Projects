import socket
import threading

# Create a dictionary to store client sockets and their names
client_sockets = {}
client_names = {}

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address (host and port)
server_host = '127.0.0.1'  # You can change this to your server IP address
server_port = 12345

# Bind the socket to the server address
server_socket.bind((server_host, server_port))

# Listen for incoming connections (max 5 clients in the queue)
server_socket.listen(5)
print(f'Server is listening on {server_host}:{server_port}')


def handle_client(client_socket, client_name):
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8')

            if not data:
                break

            # Split the message into the recipient and the actual message
            recipient, message = data.split(":", 1)

            if recipient == 'all':
                # Broadcast the message to all connected clients except the sender
                for name, socket in client_sockets.items():
                    if socket != client_socket:
                        socket.send(f'{client_name}: {message}'.encode('utf-8'))
                        client_socket.send(f'Message sent to {name}'.encode('utf-8'))
            elif recipient in client_sockets:
                # Send the message to the specified client
                recipient_socket = client_sockets[recipient]

                if client_name == 'B' and recipient in ('D', 'E', 'F'):
                    client_socket.send("You are not allowed to send messages to this recipient.".encode('utf-8'))
                else:
                    recipient_socket.send(f'{client_name}: {message}'.encode('utf-8'))
                    client_socket.send(f'Message sent to {recipient}'.encode('utf-8'))
            else:
                client_socket.send("Recipient not found".encode('utf-8'))
        except Exception as e:
            print(f"Error handling client: {e}")
            break

    # Remove the client from the dictionary when they disconnect
    del client_names[client_socket]
    del client_sockets[client_name]
    client_socket.close()
    print(f'{client_name} has disconnected.')


while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f'Accepted connection from {client_address}')

    # Receive the client's name
    client_name = client_socket.recv(1024).decode('utf-8')

    # Store the client socket and name in the dictionary
    client_sockets[client_name] = client_socket
    client_names[client_socket] = client_name

    # Print a message indicating which client has connected
    print(f'{client_name} has connected.')

    # Create a thread to handle the client's messages
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_name))
    client_thread.start()
