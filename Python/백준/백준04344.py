n = int(input())
std_list = ''
for i in range(n):
    man = 0
    sums = 0
    info = input()
    std_list = list(map(int, info.split(' ')))
    for j in range(1, int(len(std_list))):
        sums += std_list[j]
    avg = sums/std_list[0]
    for j in range(1, int(len(std_list))):
        if std_list[j] > avg:
            man += 1
    print(f'{man/(len(std_list)-1) * 100:0.3f}%')