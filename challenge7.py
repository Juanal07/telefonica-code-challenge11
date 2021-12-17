"""
I discovered the exit with brute force (19,17)
"""
# netcat codechallenge-daemons.0x14.net 4321
import socket, random
import numpy as np
import json
host = 'codechallenge-daemons.0x14.net'
port = 4321
remote_ip = socket.gethostbyname(host)
dump='q_table25.txt'

actions=[0,1,2,3]
env=[]
q_table={
        '(0, 0)':[0,0,0,0]
        }
q_table = json.load(open(dump))
print(q_table)
# north - south - east - west - look - where am I - go to x,y - is exit? - bye

alpha = 0.1
gamma = 0.6
epsilon = 0.3 #decrecerlo cuando vaya pasando el tiempo

iteraciones=100000
i=0
while i<iteraciones:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((remote_ip, port))
    intro = s.recv(1024).decode('utf-8')
    if intro =="Oh, no! You took too much time to exit. An orc caught you. The beast nails his orc sword in your chest. You die in the darkness of the maze...":
        print('se metio correctamente en el break cuando se acaba el tiempo')
        break
    actual_pos = '(0, 0)'

    while 1:
        if random.uniform(0, 1) < epsilon:
            action=random.choice(actions)
        else:
            action = np.argmax(q_table[actual_pos])
        if action == 0:
            s_action = 'north'
        elif action == 1:
            s_action = 'south'
        elif action == 2:
            s_action = 'west'
        else:
            s_action = 'east'

        s.send(bytes(s_action,'utf-8'))
        recibo = s.recv(1024).decode('utf-8').replace('\n','')
        if recibo=="Oh, no! You took too much time to exit. An orc caught you. The beast nails his orc sword in your chest. You die in the darkness of the maze...":
            print('se metio correctamente en el break cuando se acaba el tiempo')
            break

        s.send(bytes('where am I','utf-8'))
        next_pos = s.recv(1024).decode('utf-8').replace('\n','')
        if next_pos=="Oh, no! You took too much time to exit. An orc caught you. The beast nails his orc sword in your chest. You die in the darkness of the maze...":
            print('se metio correctamente en el break cuando se acaba el tiempo')
            break
        if q_table.get(next_pos)==None:
            q_table[next_pos]=[0,0,0,0]

        s.send(bytes('is exit?','utf-8'))
        data = s.recv(1024).decode('utf-8').replace('\n','')
        if data=="Oh, no! You took too much time to exit. An orc caught you. The beast nails his orc sword in your chest. You die in the darkness of the maze...":
            print('se metio correctamente en el break cuando se acaba el tiempo')
            break
        if data == 'No. Sorry, traveller...':
            if actual_pos==next_pos:
                reward=-10
            else:
                reward=-1
            old_value = q_table[actual_pos][action]
            next_max = np.max(q_table[next_pos])
            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
            q_table[next_pos][action] = new_value
        else:
            print('GAnamos o se acabo el tiempo???')
            print('ENCONTRADOOO\n\n\n\n\neeeeah\n\n')
            print(data)
            reward=100
            old_value = q_table[actual_pos][action]
            next_max = np.max(q_table[next_pos])
            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
            q_table[next_pos][action] = new_value
            json.dump(q_table, open(dump,'w'))
            break
        i+=1
        actual_pos=next_pos
        if i % 100 == 0:
            json.dump(q_table, open(dump,'w'))
            print(f"Episode: {i}")
            print(next_pos)
            # print(q_table)
        if i > iteraciones:
          break
    print("Connection closed.") 
    s.close()
json.dump(q_table, open(dump,'w'))

