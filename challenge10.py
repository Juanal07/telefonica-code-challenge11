
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
        info = input.readline()
        if not header:
                break
        header=header.split(',')
        seq=header[1].split(' ')
        list.append((int(seq[2]),info))
    # print(list)
    list_sorted = sorted(list, key=lambda x: x[0])
    # print(list_sorted)
    # for l in list_sorted:
    #     print(l)

    for l in list:
        print(l)


        # f.write('Case #{}: {}'.format(i,num_colisiones))
        # f.write('\n')
    # f.close()

# input = open('sampleInput.txt', 'r')
# input = open('testInput.txt', 'r')
input = open('icmps.txt', 'r')
challenge10(input)
input.close()

