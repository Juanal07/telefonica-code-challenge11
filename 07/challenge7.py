"""
i get stucked for 40 hours tring to do it with reinforcement learning 
finaliy did it more simple, just traversing the graph and using A* algorithm from a library
"""
import networkx as nx
import matplotlib.pyplot as plt
import socket, random
import numpy as np
import json

# netcat codechallenge-daemons.0x14.net 4321
host = 'codechallenge-daemons.0x14.net'
port = 4321
remote_ip = socket.gethostbyname(host)
dump='q_table28.txt'

G = nx.Graph()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((remote_ip, port))
intro = s.recv(1024).decode('utf-8')

s.send(bytes('where am I','utf-8'))
pos = s.recv(1024).decode('utf-8').replace('\n','')
initial = pos
cola=[]
i=0
exitDoor=''
while 1:

    # s.send(bytes('where am I','utf-8'))
    # pos = s.recv(1024).decode('utf-8').replace('\n','')
    # print(pos)

    s.send(bytes('look','utf-8'))
    look = s.recv(1024).decode('utf-8').replace('\n','')
    look = look.split(': ')
    actions = look[1].split(' ')
    print('Acciones: ',actions) # posible fallo al hacer el split cuando no haya acciones
    print('Posicion actual:',pos)
    dest=pos.replace('(','').replace(')','').replace(' ','').split(',')
    for a in actions:
        if a == 'north':
            part1=str(int(dest[1])+1)
            destino='('+dest[0]+', '+part1+')'
            arco = (pos, destino)
            if arco[1] in list(G.nodes):
                print('no lo añado')
            else:   
                cola.append([arco,a])
        if a == 'south':
            part1=str(int(dest[1])-1)
            destino='('+dest[0]+', '+part1+')'
            arco = (pos, destino)
            if arco[1] in list(G.nodes):
                print('no lo añado')
            else:   
                cola.append([arco,a])
        if a == 'west':
            part0=str(int(dest[0])+1)
            destino='('+part0+', '+dest[1]+')'
            arco = (pos, destino)
            if arco[1] in list(G.nodes):
                print('no lo añado')
            else:   
                cola.append([arco,a])
        if a == 'east':
            part0=str(int(dest[0])-1)
            destino='('+part0+', '+dest[1]+')'
            arco = (pos, destino)
            if arco[1] in list(G.nodes):
                print('no lo añado')
            else:   
                cola.append([arco,a])
        # print('Cola:',cola)
    print(cola)
    try:
        if pos!=cola[0][0][0]:
            goto=cola[0][0][0].replace('(','').replace(')','').replace(' ','')
            print('Go To: ',goto)
            s.send(bytes('go to {}'.format(goto),'utf-8'))
            goto = s.recv(1024).decode('utf-8').replace('\n','')
    except:
        break

    G.add_edge(*cola[0][0])
    # print(G.number_of_nodes())
    # print(G.number_of_edges())
    print('Accion',cola[0][1])
    s.send(bytes(cola[0][1],'utf-8'))
    msg = s.recv(1024).decode('utf-8').replace('\n','')

    s.send(bytes('where am I','utf-8'))
    pos = s.recv(1024).decode('utf-8').replace('\n','')
    print('Nueva pos',pos)
    del cola[0]
    # print('cola menos 1',cola)

    s.send(bytes('is exit?','utf-8'))
    isExit = s.recv(1024).decode('utf-8').replace('\n','')
    if isExit=='Yes. Congratulations, you found the exit door':
        exitDoor=pos
    print(isExit)
    # print('cola',cola)
    i+=1

print(G.nodes())

subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
plt.savefig("path.png")
solucion=nx.astar_path(G, initial, exitDoor)
print(solucion)

f = open("testOutput.txt", "w")
for sol in solucion:
    if sol==exitDoor:
        print(sol,end="")
        f.write(sol)
    else:
        print(sol+', ',end="")
        f.write(sol+', ')
f.close()
