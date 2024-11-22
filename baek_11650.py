# baek_11650
# 좌표 정렬하기

import sys

n = int(sys.stdin.readline())
coor_list = []

for i in range(n):
    x_i, y_i = map(int, sys.stdin.readline().split())
    coor_list.append([x_i, y_i])

coor_list.sort()

for i in coor_list:
    print(f'{i[0]} {i[1]}')




# n = int(sys.stdin.readline())
# x_list = []
# y_list = []

# for i in range(n):
#     x_i, y_i = map(int, sys.stdin.readline().split())
#     x_list.append(x_i)
#     y_list.append(y_i)

# x_list.sort()
# y_list.sort()

# for i in range(n):
#     print(f'{x_list[i]} {y_list[i]}')
    

    