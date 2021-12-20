from itertools import combinations

def challenge11(input):
    # f = open("sampleOutput.txt", "w")
    # f = open("testOutput.txt", "w")
    # f = open("submitOutput.txt", "w")
    cases = int(input.readline())
    i=1
    while i<=cases:
        print('--------------------Case: ',i)
        second = input.readline().split(' ')
        n=int(second[0])
        k=int(second[1])
        *comb, = combinations(list(range(n)), k)
        funciones=[]
        for _ in range(n):
            func=input.readline().replace('\n','')
            funciones.append(func)
        if k==1:
            mcm_raro=len(max(funciones, key=lambda x: len(x)) )
            print('SOLUCION',mcm_raro)
        else:
            mcm_max=0
            mcm=0
            # print(cob)
            for c in comb:
                encontrado=False
                j=0
                if mcm>mcm_max:
                    mcm_max=mcm
                mcm=0
                # print('combinacion',c)
                while not(encontrado):
                    for n in c:
                        if n == c[0]:
                            try:
                                letra_vieja=funciones[n][j]
                            except:
                                encontrado=True
                                break
                        else:
                            # print('funcion numero(n)',n,'letra en posicion(j):',j)
                            try:
                                letra_nueva=funciones[n][j]
                            except:
                                encontrado=True
                                break
                            # print('letra vieja->',letra_vieja,'letra nueva->',letra_nueva )
                            if letra_nueva!=letra_vieja:
                                # print('mcm')
                                encontrado=True
                                break
                            letra_vieja=letra_nueva
                    if not(encontrado):
                        mcm+=1
                    j+=1
                    # print('--> mcm: ',mcm)
            print('SOLUCION',mcm_max)
        i+=1
        



    #     f.write('Case #{}: {}'.format(i,num_colisiones))
    #     f.write('\n')
    #     i+=1
    # f.close()

input = open('sampleInput.txt', 'r')
# input = open('testInput.txt', 'r')
# input = open('submitInput.txt', 'r')
challenge11(input)
input.close()

