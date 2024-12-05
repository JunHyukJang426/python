# baek_2563
# 색종이

import sys

n = int(sys.stdin.readline())

paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    width, height = map(int, sys.stdin.readline().split())
    for x in range(width, width+10):
        for y in range(height, height+10):
            if x>=100 or y>=100:
                break
            paper[x][y] = 1
sum = 0
for i in range(100):
    sum += paper[i].count(1)
    
print(sum)
    
    