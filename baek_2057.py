# baek_2507
# 팩토리얼 분해

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

import sys

n = int(sys.stdin.readline())


fact = []
for i in range(0, 21):
    fact.append(factorial(i))


sum = 0

for i in range(20, -1, -1):
    if sum + fact[i] < n:
        sum += fact[i]
    elif sum + fact[i] == n:
        print("YES")
        exit(0)
print("NO")    