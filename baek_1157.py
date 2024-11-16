# baek_1157
# 단어 공부

word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
    count = word.count
    cnt.append(count(i))
    
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))])

    
# 틀린 코드
# string = input().lower()
# string_lst = list(set(string))
# lst = []

# for i in string:
#     count = string.count(i)
#     lst.append(count)


# if lst.count(max(lst)) > 1:
#     print('?')
# else:
#     print(string_lst[lst.index(max(lst))].upper())