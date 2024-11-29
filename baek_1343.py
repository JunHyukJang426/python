# baek_1343
# 폴리오미노

import sys

input = sys.stdin.readline()

board = str(input)
new = ''
idx = 0

while len(board) > idx:
    if board[idx:idx+4] == 'XXXX':
        new += 'AAAA'
        idx += 4
    elif board[idx:idx+2] == 'XX':
        new += 'BB'
        idx += 2
    elif board[idx] == 'X':
        newboard = -1
        print('-1')
        exit(0)
    else:
        new += board[idx]
        idx += 1
print(new)