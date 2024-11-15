# baek_2693
# N번째 큰 수

n = int(input())

for i in range(n):
    num_arr = list(map(int, input().split()))
    num_arr.sort()
    print(num_arr[-3])
    #print(*(num_arr[-3:-2]))