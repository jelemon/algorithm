N,M = input().split()
N = int(N)
M = int(M)

basket = []
for i in range(1,N+1):
    basket.append(i)

for trans in range(M):
    i,j = input().split()
    i = int(i)
    j = int(j)

    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp

print(*basket)