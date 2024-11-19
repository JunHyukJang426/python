# baek_1181
# 단어 정렬

n = int(input())
dic_list = []
result = []

for i in range(n):
    dic_list.append(input())
    
for i in dic_list:
    if i not in result:
        result.append(i)
        
result.sort()
result.sort(key=len)

for i in result:
    print(i)

