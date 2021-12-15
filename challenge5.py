import re

with open('Invictus.txt') as f:
    lines = f.readlines()
# print(lines)
# print(r'{}'.format(lines[2]))
unicodes=[]
# print(m.group(0))
for l in lines:
    # print(repr(l))
    # x = re.findall("U000e(.{4})",l)
    string = repr(l)
    # print(type(string))
    # print(string)

    match = re.search(r"U000e(.{4})", string)
    # match = re.match(r"d", string[3])
    if match:
      print(chr(int(match.group(1),16)))
      print(match.group())
      # print('ENcontraoooo')
    else:
      print("pattern not found")
    # unicodes.append(l.replace('Out',''))
    # print(r'\U000e0077')

#     # print(u'\u323')
#     unicodes.append(m)
    # unicodes.append(l.replace('Out',''))
# print(unicodes)
# print(lines)


import re

string = '39801 356, 2102 1111'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string) 

if match:
  print(match.group())
else:
  print("pattern not found")

# print(b'\U000e0077'.decode("utf-8", "strict"))
# \U000e0077
# print('\U000e007c'.decode('utf8'))
# print(ord('\u0077'))
# print(ord('\u0077'))

# print('0077','\u0077')
# print('007c','\u007c')
# print('0084','\u0084')
# print('0054','\u0054')
# print('\u0077')
# print('\u0071')
#
# print('\u0082')
# print('\u0083')
# print('\u0081')
# print('\u008d')
# print('\u0073')
# print('\u007c')
#
