from binarytree import Node

def recursiva(escala,notes,num_tonos,v):
    if len(escala)==8 and escala[0]==escala[1]:
        return True
    else:

    # if (not(len(escala)==7) and escala[0]!=notes[num_tonos[0]][v]) and escala[-1][0]!=notes[num_tonos[0]][v][0]:
    #     escala.append(notes[num_tonos[0]][v])
    #     num_tonos.remove(num_tonos[0])
    #     return recursiva(escala,notes,num_tonos,v)
    # else:
    #     return recursiva(escala,notes,num_tonos,(v+1)%2)

        
def challenge4(input):
    # f = open("testOutput.txt", "w")
    # f = open("sampleOutput.txt", "w")
    notes1 = [ ('A','A'), ('A#','Bb'),('B','Cb'),('C','B#'),('C#','Db'),('D','D'),('D#','Eb'),('E','Fb'),('F','E#'),('F#','Gb'),('G','G'),('G#','Ab') ]
    notes = [ 'A', 'A#','B','C','C#','D','D#','E','F','F#','G','G#' ]
    notes_bem = [ 'A', 'Bb','Cb','C','Db','D','Eb','E','E#','Gb','G','Ab' ]
    cases = int(input.readline())
    i=1
    while i<=cases:
        nota = input.readline().replace('\n','')
        tonos = input.readline().replace('\n','')
        try:
            index = notes.index(nota)
        except:
            index = notes_bem.index(nota)
        num_tonos=[]
        escala=[]
        escala.append(nota)
        for t in tonos:
            if t=='T':
                index=(index+2)%12
            else:
                index=(index+1)%12
            num_tonos.append(index)
        # escala += recursiva(escala,notes1,num_tonos,0)
        # print(escala)
        # escala_out=''
        # for e in escala:
        #     escala_out+=e
        # print(escala_out)
        # f.write('Case #{}: {}\n'.format(i,escala_out))
        i+=1
    # f.close()

# input = open('miInput.txt', 'r')
# input = open('sampleInput.txt', 'r')
input = open('testInput.txt', 'r')
challenge4(input)
input.close()
