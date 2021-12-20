
import json
def challenge10(input):
    # f = open("sampleOutput.txt", "w")
    # f = open("testOutput.txt", "w")
    # f = open("submitOutput.txt", "w")


    # with open('out.json') as f:
    #   data = json.load(f)
    # print(data)

    list=[]
    while True:
        header = input.readline().replace('\n','')
        info = input.readline().split('|')
        if not header:
                break
        header=header.split(',')
        id=header[1].split(' ')
        seq=header[2].split(' ')
        info=info[1].replace('.','').replace('\n','')
        
        list.append((int(id[2]),int(seq[2]),info))

    list_sorted = sorted(list, key=lambda x: x[0])
    print(list_sorted)

    # lista_rara=[]
    # for l in list_sorted:
    #     letras=l[2]
    #     for letra in letras:
    #         if ord(letra)!=l[0]:
    #             lista_rara.append((l[1],letra))

    # lista_rara = sorted(lista_rara, key=lambda x: x[0])
    # print(lista_rara)
    # for l in lista_rara:
    #     print(l[1],end='')


        # f.write('Case #{}: {}'.format(i,num_colisiones))
        # f.write('\n')
    # f.close()

# input = open('sampleInput.txt', 'r')
# input = open('testInput.txt', 'r')
input = open('icmps.txt', 'r')
challenge10(input)
input.close()

