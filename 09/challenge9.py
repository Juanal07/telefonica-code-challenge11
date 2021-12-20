"""
i get the intersection between 2 sprites and then check if there is a collision
"""
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
        for _ in range(y):
            row=input.readline().replace('\n','')
            fila=[]
            for r in row:
                fila.append(int(r))
            sprite.append(fila)
        sprites.append(sprite)
        j+=1
    i=1
    while i<=cases:
        print('Caso:',i)
        movs=input.readline()
        num_colisiones=0
        spawns=[]
        for _ in range(int(movs)):
            mov=input.readline()
            mov=mov.split(' ')
            index=int(mov[0])
            coord_x=int(mov[1])
            coord_y=int(mov[2])
            spawn=[index,(coord_x,coord_y),(coord_x+dimensiones[index][0],coord_y+dimensiones[index][1])]
            for s in spawns:
                intereseccion=[(max(s[1][0],spawn[1][0]),max(s[1][1],spawn[1][1])),(min(s[2][0],spawn[2][0]),min(s[2][1],spawn[2][1]))]
                if intereseccion[0][0] > intereseccion[1][0] or intereseccion[0][1] > intereseccion[1][1]:
                    pass
                else:
                    puntos_s=[(intereseccion[0][0]-s[1][0],intereseccion[0][1]-s[1][1]),(intereseccion[1][0]-s[1][0],intereseccion[1][1]-s[1][1])]
                    puntos_spawn=[(intereseccion[0][0]-spawn[1][0],intereseccion[0][1]-spawn[1][1]),(intereseccion[1][0]-spawn[1][0],intereseccion[1][1]-spawn[1][1])]
                    width=puntos_spawn[1][0]-puntos_spawn[0][0]
                    heigh=puntos_spawn[1][1]-puntos_spawn[0][1]
                    numero_s=s[0]
                    numero_spawn=spawn[0]
                    sprite_s=sprites[numero_s]
                    sprite_spawn=sprites[numero_spawn]
                    colision=False
                    for h in range(heigh):
                        for w in range(width):
                            eje_x_s=puntos_s[0][0]+w
                            eje_y_s=puntos_s[0][1]+h
                            eje_x_spawn=puntos_spawn[0][0]+w
                            eje_y_spawn=puntos_spawn[0][1]+h
                            valor_s=sprite_s[eje_y_s][eje_x_s]
                            valor_spawn=sprite_spawn[eje_y_spawn][eje_x_spawn]
                            if valor_s==1 and valor_spawn==1:
                                colision=True
                                num_colisiones+=1
                                break
                        if colision==True:
                            break
            spawns.append(spawn)
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

