# baek_1436
# 영화감독 숌

import sys

n = int(sys.stdin.readline())

cnt = 0
result = 666

while True:
    if '666' in str(result):
        cnt += 1
    if cnt == n:
        break
    result += 1
print(result)