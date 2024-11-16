# baek_2751
# 수 정렬하기 2

import sys

n = int(input())
n_list = []

for _ in range(n):
    n_list.append(int(sys.stdin.readline()))

n_list = list(set(n_list))
n_list.sort()
for k in n_list:
    print(k)

# 맞는데 백준 시간 초과....
# for i in range(n):
#     i = int(input())
#     n_list.append(i)
# for i in range(len(n_list)):
#     for j in range(len(n_list) - 1 - i):
#         if(n_list[j] > n_list[j+1]):
#             n_list[j+1], n_list[j] = n_list[j], n_list[j+1]
