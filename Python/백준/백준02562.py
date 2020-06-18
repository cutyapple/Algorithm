max = [0, 0]
for i in range(9):
    a = int(input())
    if max[0] < a:
        max = [a, i+1]
print(f'{max[0]}\n{max[1]}')