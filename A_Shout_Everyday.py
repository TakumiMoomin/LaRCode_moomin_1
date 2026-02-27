'''
2024-08-17(土) 21:00 ~ 2024-08-17(土) 22:40 (100分)
AtCoder Beginner Contest 367
https://atcoder.jp/contests/abc367/tasks/abc367_a
'''
#入力を受け取る
a, b, c = map(int, input().split())

#出力
if b < c:
    if b < a < c:
        print('No')
    else:
        print('Yes')
else:
    if c < a < b:
        print('Yes')
    else:
        print('No')
