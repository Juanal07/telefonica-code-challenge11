def challenge9(input):
    # f = open("sampleOutput.txt", "w")
    # f = open("testOutput.txt", "w")
    f = open("submitOutput.txt", "w")
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
        print('Caso:',i)
        movs=input.readline()
        lista_sprites=[]
        num_colisiones=0
        colision=False
        for _ in range(int(movs)):
            colision=False
            mov=input.readline()
            mov=mov.split(' ')
            new_sprite=[]
            for e in sprites[int(mov[0])]:
                tupla=(e[0]+int(mov[1]),e[1]+int(mov[2]))
                new_sprite.append(tupla)
            for l in lista_sprites:
                for n in new_sprite:
                    colision = n in l
                    if colision==True:
                        num_colisiones+=1
                        break
            lista_sprites.append(new_sprite)
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

