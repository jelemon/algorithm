N = int(input())
P = list(map(int, input().split()))

P.sort()

total = 0
current = 0

for t in P:
    current += t
    total += current

print(total)