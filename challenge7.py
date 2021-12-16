import re
"""
I find the hiden hex unicodes
pass to decimal and sub 46 (46 because I iterated until i find the right number)
pass to utf8
"""
with open('Invictus.txt') as f:
    lines = f.readlines()
unicodes=[]
for l in lines:
    string = repr(l)
    match = re.findall(r"U000e00(.{2})", string)
    unicodes+=match
mensaje=''
for u in unicodes:
    mensaje+=(chr((int(u,16))-46))
print(mensaje)

f = open("submitOutput.txt", "w")
f.write(mensaje)
f.close()

# netcat codechallenge-daemons.0x14.net 4321
