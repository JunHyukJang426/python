# baek_3052
# 나머지

num_list = []
re = []

for i in range(10):
    num_list.append(int(input()) % 42)

for i in num_list:
    if i not in re:
        re.append(i)
print(len(re))
