N = int(input())
num = input().strip()

if N > 100 or N < 1:
    exit()

total = 0

for i in num:
    total += int(i)
    if len(num) > N or len(num) < N:
        exit()

print(total)