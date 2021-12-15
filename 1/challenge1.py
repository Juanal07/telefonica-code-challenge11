"""
I read the first line as index for my loop,
then I split in 2 parts and add them together plus 1
(in the second part of the dice I have to take only the first character cause '\n' is behind)
if is 13 I do the else statement '-'
write in a output file
"""

def challenge1(input):
    f = open("submitOutput.txt", "w")
    tiradas = int(input.readline())
    i=1
    while i<=tiradas:
        line = input.readline()
        dice = line.split(':',1)
        suma = int(dice[0])+int(dice[1][0])+1
        if suma != 13:
            f.write('Case #{}: {}\n'.format(i,suma))
        else:
            f.write('Case #{}: -\n'.format(i))
        i+=1   
    f.close()

input = open('submitInput.txt', 'r')
challenge1(input)
input.close()
