import socket
from config import (
    message_size, 
    max_conn, 
    host, 
    port
)
from init import reciever_socket

# SERVER

def setup(receiver_socket, host, port):

    '''
    Args:   socket -> This refers to server socket 
            host -> This refers to the host address 
            port -> This refers to the port which will be exposed

    Func:   Setup the connection

    '''

    receiver_socket.bind((host, port))
    receiver_socket.listen(max_conn)
    conn, address = receiver_socket.accept()

    print(f"Connected to {address}")

    return (
        conn
    )

def update(conn):

    # Received a message 
    message = conn.recv(message_size)
    # Send the acknowledgement 
    acknowledgement = "Message Recieved!"
    conn.send(acknowledgement.encode())

    print('Received from server:', message.decode())

    return 

def run():

    conn = setup(
            receiver_socket=reciever_socket,
            host='',
            port=port
    )

    while True:

        try:
            update(conn)
        except Exception as e:
            print("Exception as {e}")

if __name__ == "__main__":
    run()
