a = input().strip()
b = input().strip()
c = input().strip()

vals = [a, b, c]

num = None
idx = None

for i in range(3):
    if vals[i].isdigit():
        num = int(vals[i])
        idx = i
        break

n = num + (3 - idx)

if n % 15 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)