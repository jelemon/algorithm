max_value = 0
max_row = 0
max_col = 0


for i in range(1,10):
    a = input().split()
    matrix = []
    for trans_int in a:
        matrix.append(int(trans_int))
    for j in range(1,10):
        if matrix[j-1] >= max_value:
            max_value = matrix[j-1]
            max_row = i
            max_col = j

print(max_value)
print(max_row,max_col)