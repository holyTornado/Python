"""this is test"""

# test.py

TT_DATA1 = str('abode')
TT_DATA2 = TT_DATA1
TT_DATA3 = TT_DATA2 + '123'
TT_DATA1 = TT_DATA2.upper()

print(TT_DATA1, ' : ', TT_DATA2, ' : ', TT_DATA3)

try:
    with open('missing.txt') as fileErr:
        print(fileErr.readline(), end='')
except IOError as err:
    print('File Error: ' + str(err))

print('\n' + '---9*9---')
for a in range(1, 10):
    for b in range(1, a+1):
        print(str(b) + '*' + str(a) + '=' + str(a * b) + '\t', end='')
    print('\n')

print('\n' + '---打印100内的素数---')
M_COLS_S = 0
for a in range(2, 101):
    for b in range(2, a):
        if a % b == 0:
            break
    else:
        print(str(a) + '\t', end='')
        M_COLS_S = M_COLS_S+1
        if M_COLS_S == 5:
            print('\n')
            M_COLS_S = 0

# 打印空心等边三角形
ROWS = int(input('打印空心等边三角形，输入行数：'))
for i in range(0, ROWS):
    for k in range(0, 2 * ROWS - 1):
        if (i != ROWS - 1) and (k == ROWS - i - 1 or k == ROWS + i - 1):
            print(" * ", end='')
        elif i == ROWS - 1:
            if k % 2 == 0:
                print(" * ", end='')
            else:
                print("   ", end='')
        else:
            print("   ", end='')
    print("\n")

"""
#!/usr/bin/env python
import string
shift = 3
choice = raw_input("would you like to encode or decode?")
word = (raw_input("Please enter text"))
letters = string.ascii_letters + string.punctuation + string.digits
encoded = ''
if choice == "encode":
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = letters.index(letter) + shift
            encoded=encoded + letters[x]
if choice == "decode":
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = letters.index(letter) - shift
            encoded = encoded + letters[x]
print(encoded)
"""
