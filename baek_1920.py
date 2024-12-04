# baek_1920
# 수 찾기

import sys

#input = sys.stdin.readline()

n = int(sys.stdin.readline())
a = sys.stdin.readline().split()


m = int(sys.stdin.readline())
m_list = sys.stdin.readline().split()

for i in m_list:
    print(1) if i in a else print(0)

# i = 0
# j = 0

# while i == len(m_list):
#     for j in range(len(a)):
#         if m_list[i] == a[j]:
#             print(1)
#         else:
#             print(0)
#     i += 1


# for i in range(len(m_list)):
#     for j in range(len(a)):
        
            
        