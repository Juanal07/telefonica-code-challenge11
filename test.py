
import socket
import re
import numpy as np
import json

host = 'codechallenge-daemons.0x14.net'
port = 4321
remote_ip = socket.gethostbyname(host)

actions=[0,1,2,3]
q_table = json.load(open("q_table4.txt"))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((remote_ip, port))
encontrado=False
posicion ='(0, 0)'
while not(encontrado):
    action = np.argmax(q_table[posicion])
    if action == 0:
        s_action = 'north'
    elif action == 1:
        s_action = 'south'
    elif action == 2:
        s_action = 'west'
    else:
        s_action = 'east'

    s.send(bytes(s_action,'utf-8'))
    pos = s.recv(1024)
    string = repr(pos)
    match = re.findall(r"position: (.{6})", string)
    try:
        next_position=match[0]
        print(next_position)
    except:
        next_position=posicion
        print(next_position)
    s.send(bytes('is exit?','utf-8'))
    data = s.recv(1024).decode('utf8')
    if data == 'Oh, no! You took too much time to exit. An orc caught you. The beast nails his orc sword in your chest. You die in the darkness of the maze...\n':
        break
    if data == 'Great movement. Here is your new position: (19, 17)\n':
        print("Received:", repr(pos))
        print('ENCONTRADOOO')
        encontrado=True
s.close()
