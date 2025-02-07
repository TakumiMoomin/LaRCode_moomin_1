'''
2024-09-14(土) 21:00 ~ 2024-09-14(土) 22:40 (100分)
AtCoder Beginner Contest 371
https://atcoder.jp/contests/abc371/tasks/abc371_a
'''
#入力を受け取る
a, b, c = input().split()

#出力
if a == '<':
    if b == '<':
        if c == '<':
            print('B')
        else:
            print('C')
    else:
        print('A')
else:
    if b == '<':
        print('A')
    else:
        if c == '<':
            print('C')
        else:
            print('B')
        