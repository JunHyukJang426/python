# baek_9012
# 괄호



# for _ in range(n):
#     xy = list(str(input()))
#     xy_1 = xy.count('(')
#     xy_2 = xy.count(')')
#     if xy_1 == xy_2:
        
#         print('YES')
#     else:
#         print('NO')

n = int(input())

for _ in range(n):
    isVPS = list(input())
    sum = 0
    for i in range(len(isVPS)):
        if isVPS[i] == '(':
            sum += 1
        else:
            sum -= 1
        
        if sum < 0:
            print('NO')
            break
        
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')
        

# 맞는데 이해가 잘 안감
# for _ in range(n):
#     isVPS = []
#     xy = input()
#     for i in xy:
#         if i == '(':
#             isVPS.append(i)
#         elif i == ')':
#             if len(isVPS) != 0:
#                 isVPS.pop()
#             else:
#                 print('NO')
#                 break
#     else:
#         if len(isVPS) == 0:
#             print('YES')
#         else:
#             print('NO')