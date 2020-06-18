n = int(input())
strs = []
results = []
for i in range(n):
    strs.append(list(input()))
    results.append(0)

for i in range(n):
    add = 0
    for j in range(len(strs[i])):
        if strs[i][j] == 'O':
            add += 1
        else:
            add = 0
        results[i] += add
for i in range(len(results)):
    print(results[i])
