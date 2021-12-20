"""
convert tickets into a graph
remove one node and test if is connected
using a lib for ease
"""
import networkx as nx

def challenge8(input):
    # f = open("sampleOutput.txt", "w")
    # f = open("testOutput.txt", "w")
    f = open("submitOutput.txt", "w")
    cases = int(input.readline())
    i=1
    while i<=cases:
        j=1
        n_tickets = int(input.readline())
        G = nx.Graph()
        while j<=n_tickets:
            tickets = input.readline().replace('\n','').split(',')
            G.add_edge(*(tickets[0],tickets[1]))
            j+=1
        lista_nodos=list(G.nodes)
        cities=[]
        for l in lista_nodos:
            aux_G=nx.Graph(G)
            aux_G.remove_node(l)
            if not(nx.is_connected(aux_G)):
                cities.append(l)
        cities.sort()
        print('Case #{}: '.format(i),end='')
        f.write('Case #{}: '.format(i))
        if len(cities)==0:
            print('-')
            f.write('-')
        for city in cities:
            if city == cities[-1]:
                print('{}'.format(city))
                f.write('{}'.format(city))
            else:
                print('{},'.format(city),end='')
                f.write('{},'.format(city))
        f.write('\n')
        i+=1
    f.close()

# input = open('sampleInput.txt', 'r')
# input = open('testInput.txt', 'r')
input = open('submitInput.txt', 'r')
challenge8(input)
input.close()

