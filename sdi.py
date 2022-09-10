import sys
from math import log

file = sys.argv[1]

with open(file, 'r') as f:
    ls = f.readlines()

ns = []
total = 0
fail = False

for l in ls:
    if l[0] != '#':
        try:
            n = int(l.strip())
            ns.append(n)
            total += n
        except:
            fail = True
            print(f'{l.strip()} is not valid integer')

if fail:
    print
    raise ValueError('please fix errors')


ps = [n/total for n in ns]

# print(ps)
prop_times_log = [p * log(p) for p in ps]

# print(prop_times_log)

sdi = round(-sum(prop_times_log),4)

print(f'SDI for {file} is: {sdi}')
