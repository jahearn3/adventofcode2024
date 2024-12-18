# Day 17: Chronospatial Computer

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

registers = {}
registers['A'] = int(data[0].split(':')[1])
registers['B'] = int(data[1].split(':')[1])
registers['C'] = int(data[2].split(':')[1])
program = [int(i) for i in data[4].split(':')[1].split(',')]
ptr = 0
output = []


def combo_operand(operand):
    if operand < 4:
        return operand
    elif operand == 4:
        return registers['A']
    elif operand == 5:
        return registers['B']
    elif operand == 6:
        return registers['C']
    elif operand == 7:
        print('Invalid program')
        return 0


def compute(opcode, operand, ptr):
    out = -1
    if opcode == 0:
        # adv: division
        numerator = registers['A']
        denominator = 2 ** combo_operand(operand)
        registers['A'] = numerator // denominator
    elif opcode == 1:
        # bxl: bitwise XOR
        registers['B'] = registers['B'] ^ operand
    elif opcode == 2:
        # bst: modulo
        registers['B'] = combo_operand(operand) % 8
    elif opcode == 3:
        # jnz: jump
        if registers['A'] != 0:
            ptr = operand
    elif opcode == 4:
        # bxc: bitwise XOR
        registers['B'] = registers['B'] ^ registers['C']
    elif opcode == 5:
        # out
        out = combo_operand(operand) % 8
    elif opcode == 6:
        # bdv: division
        numerator = registers['A']
        denominator = 2 ** combo_operand(operand)
        registers['B'] = numerator // denominator
    elif opcode == 7:
        # cdv: division
        numerator = registers['A']
        denominator = 2 ** combo_operand(operand)
        registers['C'] = numerator // denominator
    # print(registers)
    return out, ptr


# Examples
# registers['C'] = 9
# program = [2, 6]
# registers['A'] = 10
# program = [5, 0, 5, 1, 5, 4]
# registers['A'] = 2024
# program = [0, 1, 5, 4, 3, 0]
# registers['B'] = 29
# program = [1, 7]
# registers['B'] = 2024
# registers['C'] = 43690
# program = [4, 0]

# print('Before')
# print(registers)

c = 0
while c < 1000:
    try:
        opcode = program[ptr]
        operand = program[ptr+1]
    except IndexError:
        break
    # print(c, opcode, operand, ptr)
    out, new_ptr = compute(opcode, operand, ptr)
    # print(out, new_ptr)
    if ptr == new_ptr:
        ptr += 2
    else:
        ptr = new_ptr
    if out != -1:
        output.append(out)
    c += 1

# print('After')
# print(registers)
# print(output)
print(','.join([str(i) for i in output]))

# Part 2


def run_program(program, registers):
    ptr = 0
    output = []
    while True:
        try:
            opcode = program[ptr]
            operand = program[ptr+1]
        except IndexError:
            break
        out, new_ptr = compute(opcode, operand, ptr)
        if ptr == new_ptr:
            ptr += 2
        else:
            ptr = new_ptr
        if out != -1:
            output.append(out)
        # Early stopping condition
        if output != program[:len(output)]:
            break

    return output


registers['A'] = int(data[0].split(':')[1])
registers['B'] = int(data[1].split(':')[1])
registers['C'] = int(data[2].split(':')[1])
program = [int(i) for i in data[4].split(':')[1].split(',')]
# program = [0, 3, 5, 4, 3, 0]
# Program: [2, 4, 1, 6, 7, 5, 4, 6, 1, 4, 5, 5, 0, 3, 3, 0]
ptr = 0
output = []
print('Program:', program)
a = 6130000
record_length = 1
while True:
    registers['A'] = a
    output = run_program(program, registers)
    if program == output:
        break
    else:
        if len(output) > record_length:
            print(a, output)
            record_length = len(output)
        a += 1

print(a)
# 317476438 [2, 4, 1, 6, 7, 5, 4, 6, 1, 0]
