# Import socket module
import socket
from config import (
    message_size, 
    host, 
    port
)

import uuid

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
    wrapper = {
        "id": str(uuid.uuid4()),
        "message": message
    }
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

        try:
            message = input("Enter your message: ")
            update(message=message, sender_socket=sender_socket)
        except Exception as e:
            print(f"Exception as {e}")

if __name__ == "__main__":
    run()