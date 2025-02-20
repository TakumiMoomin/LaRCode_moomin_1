'''
2024-09-14(土) 21:00 ~ 2024-09-14(土) 22:40 (100分)
AtCoder Beginner Contest 371
https://atcoder.jp/contests/abc371/tasks/abc371_b
'''
#入力の受け取り
n, m = map(int, input().split())
str_list = []
for i in range(m):
    str_list.append(list(input().split()))

#出力
first_list = [list() for _ in range(n)]
for i in range(m):
    if first_list[int(str_list[i][0])-1] == [] and str_list[i][1] == 'M':
        first_list[int(str_list[i][0]-1)].append('M')
        print('Yes')
    else:
        print('No')

