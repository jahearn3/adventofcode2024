# Day 21: Keypad Conundrum

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
# data = ld.load_data(f'input{day}.txt')


def numeric_keypad(text):
    seq = ''
    pos = 'A'
    for char in text:
        while pos != char:
            if pos == 'A':
                if char == '0':
                    seq += '<'
                    pos = '0'
                else:
                    seq += '^'
                    pos = '3'
            elif pos == '0':
                if char == 'A':
                    seq += '>'
                    pos = 'A'
                else:
                    seq += '^'
                    pos = '2'
            elif int(pos) % 3 == 0:  # 3, 6, 9
                if char == 'A':
                    seq += 'v'
                    pos = str(int(pos) - 3)
                    if pos == '0':
                        pos = 'A'
                elif int(char) < int(pos):
                    seq += '<'
                    pos = str(int(pos) - 1)
                else:
                    seq += '^'
                    pos = str(int(pos) + 3)
            elif int(pos) % 3 == 2:  # 2, 5, 8
                if char == 'A' or char == '0':
                    seq += 'v'
                    pos = str(int(pos) - 3)
                    if pos == '-1':
                        pos = '0'
                elif int(char) % 3 == 1:
                    seq += '<'
                    pos = str(int(pos) - 1)
                elif int(char) % 3 == 0:
                    seq += '>'
                    pos = str(int(pos) + 1)
                elif int(char) < int(pos):
                    seq += 'v'
                    pos = str(int(pos) - 3)
                else:
                    seq += '^'
                    pos = str(int(pos) + 3)
            else:  # 1, 4, 7
                if char in ['A', '0', '2', '3', '5', '6', '8', '9']:
                    seq += '>'
                    pos = str(int(pos) + 1)
                elif int(char) < int(pos):
                    seq += 'v'
                    pos = str(int(pos) - 3)
                else:
                    seq += '^'
                    pos = str(int(pos) + 3)
        seq += 'A'
    return seq


dir_pad = '''
 ^A
<v>
'''


def directional_keypad(seq):
    new_seq = ''
    pos = 'A'
    # print('seq:', seq)
    # c = 0
    for char in seq:
        # print('char:', char)
        while pos != char:
            if pos == 'A':
                if char == '^':
                    new_seq += '<'
                    pos = '^'
                else:
                    new_seq += 'v'
                    pos = '>'
            elif pos == '^':
                if char == 'A':
                    new_seq += '>'
                    pos = 'A'
                else:
                    new_seq += 'v'
                    pos = 'v'
            elif pos == '<':
                new_seq += '>'
                pos = 'v'
            elif pos == '>':
                if char == 'A':
                    new_seq += '^'
                    pos = 'A'
                else:
                    new_seq += '<'
                    pos = 'v'
            else:  # pos == 'v'
                if char == 'A':
                    new_seq += '^'
                else:
                    new_seq += char
                pos = new_seq[-1]
            # print(pos, char, new_seq)
            # c += 1
            # if c >= 10:
            #     print('Not found')
            #     break
        new_seq += 'A'
    return new_seq


ans = 0
for line in data:
    seq0 = numeric_keypad(line)  # robot because depressurized
    seq1 = directional_keypad(seq0)  # robot because radiation
    seq2 = directional_keypad(seq1)  # robot because -40 deg
    seq3 = directional_keypad(seq2)  # human because crowded
    print(len(seq0), len(seq1), len(seq2), len(seq3))
    print(len(seq3), int(line[:3]))
    ans += len(seq3) * int(line[:3])

print(ans)
