def challenge9(input):
    # f = open("sampleOutput.txt", "w")
    # f = open("testOutput.txt", "w")
    # f = open("submitOutput.txt", "w")
    cases = int(input.readline())
    n_sprites = int(input.readline())
    j=1
    sprites=[]
    while j<=n_sprites:
        size = input.readline()
        size = size.split(' ')
        x=int(size[0])
        y=int(size[1])
        sprite=[]
        for k in range(y):
            row=input.readline()
            for d in range(x):
                if row[d]=='1':
                    sprite.append((d,k))
        sprites.append(sprite)
        j+=1
    # print(sprites)
    i=1
    while i<=cases:
        active=[0]*n_sprites
        print('Caso: ',i)
        sprites_aux=sprites.copy()
        movs=input.readline()
        num_colisiones=0
        for _ in range(int(movs)):
            mov=input.readline()
            mov=mov.split(' ')
            new_sprite=[]
            for e in sprites_aux[int(mov[0])]:
                tupla=(e[0]+int(mov[1]),e[1]+int(mov[2]))
                new_sprite.append(tupla)
            sprites_aux[int(mov[0])] = new_sprite.copy()
            # print(sprites_aux[int(mov[0])])
            # print(active)
            active[int(mov[0])]=1
            print(active)
            # print('sprite modificado',sprites_aux)
            colision=False
            for posicion_activa in range(len(active)):
                sprite_activo=int(mov[0])
                if active[posicion_activa]==1:
                    if sprite_activo!=posicion_activa:
                        for l in sprites_aux[posicion_activa]:
                            colision = l in sprites_aux[int(mov[0])]
                            if colision==True:
                                num_colisiones+=1
                                break
                if colision==True:
                    break
        # print('Colisiones',num_colisiones)
        i+=1

input = open('sampleInput.txt', 'r')
# input = open('testInput.txt', 'r')
# input = open('submitInput.txt', 'r')
challenge9(input)
input.close()

    # # f = open("submitOutput.txt", "w")
    #             f.write('{},'.format(city))
    #     f.write('\n')
    #     i+=1
    # f.close()
