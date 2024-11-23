# baek_1251
# 단어 나누기

word = input()
words = []
for i in range(1, len(word)):
    for j in range(i+1, len(word)):
        part1 = word[:i][::-1]
        part2 = word[i:j][::-1]
        part3 = word[j:][::-1]
        words.append(part1+part2+part3)
print(sorted(words)[0])        


# import random

# word = list(input())
# length = len(word)

# indices = random.sample(range(length), 2)

# part1 = word[:indices[0]]
# part2 = word[indices[0]:indices[1]]
# part3 = word[indices[1]:]

# part1.reverse()
# part2.reverse()
# part3.reverse()

# part1.sort()
# part2.sort()
# part3.sort()

# part = ''.join(part1)+''.join(part2)+''.join(part3)
# print(part)