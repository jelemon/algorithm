N = int(input())

first = N

cycle = 0

while True:
    tens = N//10
    ones = N%10
    a = tens + ones
    new_N = (ones*10) + (a%10)
    cycle += 1
    N = new_N
    if N == first:
        break

print(cycle)