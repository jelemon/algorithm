N = int(input())

row = 1
k = 0
while N > k:
    k = k + row
    if N <= k:
        break
    row += 1

standard = k - N

if row % 2 == 0:
    numerator = row - standard
    denominator = 1 + standard
else:
    numerator = 1 + standard
    denominator = row - standard

print(f"{numerator}/{denominator}")