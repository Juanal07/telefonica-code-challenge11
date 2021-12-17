def challenge8(input):
    f = open("submitOutput.txt", "w")
    cases = int(input.readline())
    i=1
    while i<=cases:
        line = input.readline().replace('\n','').split(':')
        fecha = line[0].split('-')
        if len(fecha[0])==2:
            aux = fecha[0]
            fecha[0]=fecha[2]
            fecha[2]=aux
        try:
            day_week=date(int(fecha[0]),int(fecha[1]),int(fecha[2])).weekday()
            try:
                print('Case #{}: {}'.format(i,dict[line[1]][day_week]))
                f.write('Case #{}: {}\n'.format(i,dict[line[1]][day_week]))
            except:
                print('Case #{}: {}'.format(i,'INVALID_LANGUAGE'))
                f.write('Case #{}: {}\n'.format(i,'INVALID_LANGUAGE'))
        except:
            print('Case #{}: {}'.format(i,'INVALID_DATE'))
            f.write('Case #{}: {}\n'.format(i,'INVALID_DATE'))
        i+=1
    f.close()

# input = open('miInput.txt', 'r')
# input = open('sampleInput.txt', 'r')
# input = open('testInput.txt', 'r')
input = open('submitInput.txt', 'r')
challenge6(input)
input.close()


