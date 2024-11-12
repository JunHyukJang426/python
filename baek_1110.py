# baek_1110
# 더하기 사이클

count = 0
n = n_1 = int(input())

a = []
while True:
    ten = n_1 // 10
    one = n_1 % 10
    
    n_1 = (one * 10) + ((ten + one) % 10)
    count += 1
    
    if n == n_1:
        break  
print(count)