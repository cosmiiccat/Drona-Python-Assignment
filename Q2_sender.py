# Import socket module
import socket
from config import (
    message_size, 
    host, 
    port
)

from init import sender_socket

def setup(sender_socket, host, port):

    '''
    Args:   socket -> This refers to server socket 
            host -> This refers to the host address 
            port -> This refers to the port which will be exposed

    Func:   Setup the connection

    '''

    sender_socket.connect((host, port))

    return 

def update(message, sender_socket):

    # Send a message to the server
    sender_socket.send(message.encode())
    # Receive the acknowledgement from the server
    acknowledgement = sender_socket.recv(message_size)
    print('Received from server:', acknowledgement.decode())

    return 


def run():

    setup(
        sender_socket=sender_socket,
        host=host,
        port=port
    )

    while True:
        
        message = input("Enter your message: ")
        update(message=message, sender_socket=sender_socket)

if __name__ == "__main__":
    run()