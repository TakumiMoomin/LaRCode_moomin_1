'''
2024-09-14(土) 21:00 ~ 2024-09-14(土) 22:40 (100分)
AtCoder Beginner Contest 371
https://atcoder.jp/contests/abc371/tasks/abc371_b
'''
#入力の受け取り
n, m = map(int, input().split())

#出力
first_son = [False]*(n)
for _ in range(m):
    a, b = input().split()
    a = int(a)
    
    if b == "M" and not first_son[a-1]:
        print("Yes")
        first_son[a-1] = True
    else:
        print("No")