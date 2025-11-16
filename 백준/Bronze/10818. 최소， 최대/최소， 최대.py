N = int(input())
num = map(int,input().split())

if N > 1000000 or N < 1:
    exit()

min_ = 1000000
max_ = -1000000

for i in num:
    if i < min_:
        min_ = i
    if i > max_:
        max_ = i

print(min_,max_)