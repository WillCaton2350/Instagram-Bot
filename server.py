import socket

HOST = "10.0.2.15"
PORT = 8082

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
print("Server Activated")
print("Waiting for connection...")
server.listen(1)
client, client_address = server.accept()
print(f'{client_address}:{client_address}')

while True:
    command = input('Enter command: ')
    command = command.encode()
    client.send(command)
    print('Command sent')
    output = client.recv(1024)
    print(f'Received: {output.decode()}')   
