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
G.add_node('(0 ,0)')
# G.add_edges_from([(0, 10), (10, 101)])
# G.add_edges_from([(1, 2), (1, 3),(55,33)])
print(G.nodes())

# G = nx.petersen_graph()
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
# subax2 = plt.subplot(122)
plt.savefig("path.png")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((remote_ip, port))
intro = s.recv(1024).decode('utf-8')
while 1:

    s.send(bytes('where am I','utf-8'))
    pos = s.recv(1024).decode('utf-8').replace('\n','')
    print(pos)

    s.send(bytes('look','utf-8'))
    look = s.recv(1024).decode('utf-8').replace('\n','')
    look = look.split(': ')
    actions = look[1].split(' ')
    print(actions)

    s.send(bytes(actions[0],'utf-8'))
    action = s.recv(1024).decode('utf-8').replace('\n','')

    s.send(bytes('is exit?','utf-8'))
    isExit = s.recv(1024).decode('utf-8').replace('\n','')

print(G.nodes())
