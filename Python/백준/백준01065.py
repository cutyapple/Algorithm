input_num = int(input())

def is_hansu(num):
    if num < 100:
        return 1

    num = str(num)
    num_len = len(num)
    num_list = list(num)
    minus_list = []

    for i in range(num_len - 1):
        minus = int(num_list[i]) - int(num_list[i+1])
        minus_list.append(minus)

    if num_len-1 == minus_list.count(minus_list[0]):
        return 1
    return 0

su = 0

for i in range(1, input_num+1):
    su += is_hansu(i)

print(su)
