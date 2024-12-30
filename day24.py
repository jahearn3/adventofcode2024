# Day 24: Crossed Wires

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}a.txt')
data = ld.load_data(f'example{day}b.txt')
data = ld.load_data(f'input{day}.txt')

wires = {}
gates = {}
blank = False
for line in data:
    if len(line) == 0:
        blank = True
    elif blank:
        a, b = line.split(' -> ')
        gates[b] = a
    else:
        a, b = line.split(': ')
        wires[a] = int(b)

hi_z = 0
q = []

# Simulate
for k, v in gates.items():
    input1, logic, input2 = v.split(' ')
    if input1 in wires and input2 in wires:
        if logic == 'AND':
            result = wires[input1] and wires[input2]
        elif logic == 'OR':
            result = wires[input1] or wires[input2]
        elif logic == 'XOR':
            result = wires[input1] ^ wires[input2]
        wires[k] = result
        if k[0] == 'z' and int(k[1:]) > hi_z:
            hi_z = int(k[1:])
    else:
        q.append((k, v))

i = 0
while len(q) > 0:
    k, v = q.pop(0)
    input1, logic, input2 = v.split(' ')
    if input1 in wires and input2 in wires:
        if logic == 'AND':
            result = wires[input1] and wires[input2]
        elif logic == 'OR':
            result = wires[input1] or wires[input2]
        elif logic == 'XOR':
            result = wires[input1] ^ wires[input2]
        wires[k] = result
        if k[0] == 'z' and int(k[1:]) > hi_z:
            hi_z = int(k[1:])
    else:
        q.append((k, v))


binary_string = ''
for i in range(hi_z + 1):
    if i < 10:
        k = 'z0' + str(i)
    else:
        k = 'z' + str(i)
    binary_string += str(wires[k])

# Reverse the string
n = binary_string[::-1]

# Convert from binary to decimal
print(int(n, 2))
