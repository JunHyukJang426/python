# baek_1712
# 손익분기점

# A = 고정비용 B = 가변비용
# C = 판매비용
# 판매비용 = 고정비용 + 가변비용
# ex) A = 1000, B = 70 -> 한대 생산시 A + B, 10대 생산시 A + B * 10

A, B, C = map(int, input().split())

if(B >= C):
    print(-1)
else:
    print(A // (C-B) + 1)