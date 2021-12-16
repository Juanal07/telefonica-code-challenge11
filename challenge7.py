"""
I discovered the exit with brute force (19,17)

"""
# netcat codechallenge-daemons.0x14.net 4321
import socket, random
import re
import numpy as np
import json
host = 'codechallenge-daemons.0x14.net'
port = 4321
remote_ip = socket.gethostbyname(host)

actions=[0,1,2,3]
env=[]
q_table={
        '(0, 0)':[0,0,0,0],
        }
q_table = json.load(open("q_table.txt"))
print(q_table)
# reward_table={
#         '(x, x)':{'north':-1, 'south':-1,'west':-1,'east':-1},
#         '(18, 17)':{'north':100, 'south':-1,'west':-1,'east':-1},
#         '(20, 17)':{'north':-1, 'south':100,'west':-1,'east':-1},
#         '(19, 16)':{'north':-1, 'south':-1,'west':100,'east':-1},
#         '(19, 18)':{'north':-1, 'south':-1,'west':-1,'east':100},
# }

# north - south - east - west - look - where am I - go to x,y - is exit? - bye

# Hyperparameters
alpha = 0.1
gamma = 0.6
epsilon = 0.1 #decrecerlo cuando vaya pasando el tiempo

# For plotting metrics
all_epochs = []
all_penalties = []

encontrado=False
iteraciones=10000
i=0
while i<iteraciones:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((remote_ip, port))
    next_position ='(0, 0)'
    # epochs, penalties, reward, = 0, 0, 0

    print('Epoch: ',i)
    while 1:
        posicion=next_position

        if random.uniform(0, 1) < epsilon:
            action=random.choice(actions)
        else:
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
        match = re.findall(r"position: (\(.*\))", string)
        next_position=''
        try:
            next_position=match[0]
            # print(next_position)
            if q_table.get(next_position)==None:
                q_table[next_position]=[0,0,0,0]
                # print(q_table)
        except:
            next_position=posicion
            # print(next_position)
        # print(next_position)

        reward=-1
        old_value = q_table[posicion][action]
        # print(old_value)
        next_max = np.max(q_table[next_position])
        # print(next_max)
        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        # print('new value: ',new_value)
        q_table[posicion][action] = new_value

        s.send(bytes('is exit?','utf-8'))
        data = s.recv(1024).decode('utf8')
        if data == 'Oh, no! You took too much time to exit. An orc caught you. The beast nails his orc sword in your chest. You die in the darkness of the maze...\n':
            json.dump(q_table, open("q_table.txt",'w'))
            break
        if data == 'Great movement. Here is your new position: (19, 17)\n':
            print("Received:", repr(pos))
            print('ENCONTRADOOO')
            reward=100
            old_value = q_table[posicion][action]
            print(old_value)
            next_max = np.max(q_table[next_position])
            print(next_max)
            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
            print('new value: ',new_value)
            q_table[posicion][action] = new_value

            # encontrado=True

            json.dump(q_table, open("q_table.txt",'w'))
            break
        i+=1
        # epsilon-=1/iteraciones
        if i % 100 == 0:
            json.dump(q_table, open("q_table.txt",'w'))
            print(f"Episode: {i}")
            print(next_position)
        if i > iteraciones:
          json.dump(q_table, open("q_table.txt",'w'))
          break
        # print(epsilon)
        # print('Epoch: ',i)
    print("Connection closed.") 
    s.close()
# Oh, no! You took too much time to exit. An orc caught you. The beast nails his orc sword in your chest. You die in the darkness of the maze...\n



f = open("q_table.txt", "w")
f.write(str(q_table))
f.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((remote_ip, port))

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
