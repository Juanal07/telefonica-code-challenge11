def challenge9(input):
    # f = open("sampleOutput.txt", "w")
    # f = open("testOutput.txt", "w")
    f = open("submitOutput.txt", "w")
    cases = int(input.readline())
    n_sprites = int(input.readline())
    j=1
    sprites=[]
    dimensiones=[]
    while j<=n_sprites:
        size = input.readline()
        size = size.split(' ')
        x=int(size[0])
        y=int(size[1])
        dimen=(int(x),int(y))
        dimensiones.append(dimen)
        sprite=[]
        for k in range(y):
            row=input.readline()
            for d in range(x):
                if row[d]=='1':
                    sprite.append((d,k))
        sprites.append(sprite)
        j+=1
    # print(dimensiones)
    # print(sprites)
    i=1
    while i<=cases:
        print('Caso:',i)
        movs=input.readline()
        lista_sprites=[]
        num_colisiones=0
        colision=False
        for _ in range(int(movs)):
            colision=False
            mov=input.readline()
            mov=mov.split(' ')
            coord_x=int(mov[1])
            coord_y=int(mov[2])
            new_sprite=[]
            for e in sprites[int(mov[0])]:
                tupla=(e[0]+coord_x,e[1]+coord_y)
                new_sprite.append(tupla)
            val=[coord_x,coord_x+dimensiones[int(mov[0])][0],coord_y,coord_y+dimensiones[int(mov[0])][1]]
            # print(val)
            for l in lista_sprites:
                for n in new_sprite:
                    if l[1][0]>val[1] or l[1][1]<val[0] or l[1][2]>val[3] or l[1][3]<val[2]:
                        break
                    colision = n in l[0]
                    if colision==True:
                        num_colisiones+=1
                        break
            lista_sprites.append([new_sprite,val])
        print('Colisiones:',num_colisiones)
        f.write('Case #{}: {}'.format(i,num_colisiones))
        f.write('\n')
        i+=1
    f.close()

# input = open('sampleInput.txt', 'r')
# input = open('testInput.txt', 'r')
input = open('submitInput.txt', 'r')
challenge9(input)
input.close()

