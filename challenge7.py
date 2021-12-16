# netcat codechallenge-daemons.0x14.net 4321
# from netcat import Netcat
import socket, sys, time
host = 'codechallenge-daemons.0x14.net'
port = 4321

remote_ip = socket.gethostbyname(host)
print(remote_ip)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((remote_ip, port))
while 1:
    s.send(bytes('west','utf-8'))
    data = s.recv(1024)
    if data == "":
        break
    print("Received:", repr(data)) 
print("Connection closed.") 
s.close()
