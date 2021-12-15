import re
with open('Invictus.txt') as f:
    lines = f.readlines()
print(lines)
# print(b'\U000e0077'.decode("utf-8", "strict"))
unicodes=[]
# print(m.group(0))
for l in lines:
    m = re.search('U.{8}', l)
    # print(u'\u323')
    unicodes.append(l.replace('Out',''))
print(unicodes)



