def challenge4(input):
    notes = [ 'A', ('A#','Bb'),'B','C',('C#','Db'),'D',('D#','Eb'),'E','F',('F#','Gb'),'G',('G#','Ab') ]
    # notes = [ 'A', 'A#','B','C','C#','D','D#','E','F','F#','G','G#' ]
    # notes2 = [ 'A', 'Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab' ]
    print('Notas: ', notes)
    print('N¤ de notas: ', len(notes))
    cases = int(input.readline())
    i=1
    while i<=cases:
        nota = input.readline().replace('\n','')
        print('Nota: ', nota) #Bb
        try:
            index = notes.index(nota)
        except:
            index = notes.index(nota)
        print('Index: ',index)
        tonos = input.readline().replace('\n','')
        print(tonos)
        escala=nota
        for t in tonos:
            if t=='T':
                index=(index+2)%12
            else:
                index=(index+1)%12
            try:
                escala+=notes[index]
            except:
                escala+=notes[index][0]
        print(escala)
        i+=1

input = open('testInput.txt', 'r')
# input = open('sampleInput.txt', 'r')
challenge4(input)
input.close()
