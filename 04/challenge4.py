"""
I have to test all possibilities until i find the right one
64 posibilities cause the first and the last one note is known
probably better optimization with some kind of binary tree
"""
def challenge4(input):
    # f = open("sampleOutput.txt", "w")
    # f = open("testOutput.txt", "w")
    f = open("submitOutput.txt", "w")
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
        for t in tonos:
            if t=='T':
                index=(index+2)%12
            else:
                index=(index+1)%12
            num_tonos.append(index)
        j=0
        encontrado=False
        escala=[]
        while j<64 and not(encontrado):
            escala=[]
            escala.append(nota)
            bin = '{0:06b}'.format(j)
            for b in range(6):
                if escala[-1][0]!=notes1[num_tonos[b]][int(bin[b])][0]:
                    escala.append(notes1[num_tonos[b]][int(bin[b])])
                else:
                    break
            if escala[-1][0]!=escala[0][0] and len(escala)==7:
                escala.append(escala[0])
                encontrado=True
            j+=1
        escala_out=''
        for e in escala:
            escala_out+=e
        print(escala_out)
        f.write('Case #{}: {}\n'.format(i,escala_out))
        i+=1
    f.close()

# input = open('sampleInput.txt', 'r')
# input = open('testInput.txt', 'r')
input = open('submitInput.txt', 'r')
challenge4(input)
input.close()

