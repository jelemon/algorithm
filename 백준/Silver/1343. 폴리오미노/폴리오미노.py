s = input()

result = ""
i = 0
n = len(s)

while i < n:

    if s[i] == '.':
        result += '.'
        i += 1
        continue

    j = i
    while j < n and s[j] == 'X':
        j += 1
    length = j - i

    if length % 2 == 1:
        print(-1)
        exit()

    result += "AAAA" * (length // 4)
    result += "BB" * ((length % 4) // 2)

    i = j

print(result)