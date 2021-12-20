"""
The interesting parts here are the cleaning of the diferent format dicts
and the exception of fractions values
I not sure if i make a mistake with some borderline float sums.
At least the test is passed 😼
"""

def challenge3(input):
  f = open("submitOutput.txt", "w")
  n = int(input.readline())
  for i in range(1,n+1):
    line = input.readline().replace('\n','').split('|')
    antonyms = line[0].split('-')
    d={}
    if line[1][0]=='{':
      line = line[1].strip('{}').replace("'",'').replace(" ",'').split(',')
    elif line[1][0]=='[':
      line = line[1].strip('[]').replace(')','').replace('(','').replace("',",':').replace("'",'').replace(" ",'').split(',')
    else:
      line = line[1].replace('=',':').split(',')
    for l in line:
      l = l.split(':')
      try:
        d[l[0]]=float(l[1])
      except:
        frac=l[1].split('/')
        d[l[0]]=float(int(frac[0])/int(frac[1]))
    sum_first=0
    sum_sec=0
    for l in antonyms[0]:
      sum_first+=d.get(l)
    for l in antonyms[1]:
      sum_sec+=d.get(l)
    if sum_first==sum_sec:
      f.write('Case #{}: -'.format(i))
      f.write('\n')
    elif sum_first > sum_sec:
      f.write('Case #{}: {}'.format(i,antonyms[0]))
      f.write('\n')
    else:
      f.write('Case #{}: {}'.format(i,antonyms[1]))
      f.write('\n')
  f.close()

input = open('submitInput.txt', 'r')
challenge3(input)
input.close()
