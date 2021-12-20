def challenge2(input):
    f = open("submitOutput.txt", "w")
    n = int(input.readline())
    i=1
    while i<=n:
        values = input.readline().split(' ')
        pokemons = []
        num_pokemons = int(values[0])
        for _ in range(num_pokemons):
            pokemon = input.readline().replace('\n',' ').replace(' ','')
            pokemons.append(pokemon)
        sopa=''
        rows_sopa = int(values[1])
        for _ in range(rows_sopa):
            sopa+=input.readline().replace('\n','').replace(' ','')
        p=0
        while len(pokemons)!=0:
            if pokemons[p] in sopa:
              sopa = sopa.replace(pokemons[p],'')
              pokemons.remove(pokemons[p])
              p=0
            elif pokemons[p][::-1] in sopa:
              sopa = sopa.replace(pokemons[p][::-1],'')
              pokemons.remove(pokemons[p])
              p=0
            else:
              p+=1
        f.write('Case #{}: {}\n'.format(i,sopa))
        i+=1
    f.close()

input = open('submitInput.txt', 'r')
challenge2(input)
input.close()
