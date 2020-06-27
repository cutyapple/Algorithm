def self_num():
    arr = list()
    res = 0
    for i in range(1, 10001):
        if i < 10:
            res = i + i
            arr.append(res)
        elif i < 100:
            res = i + (i // 10) + (i % 10)
            arr.append(res)
        elif i < 1000:
            res = i + (i // 100) + ((i % 100) // 10) + ((i % 100) % 10)
            arr.append(res)
        elif i < 10000:
            res = i + (i // 1000) + ((i % 1000) // 100) + (((i % 1000) % 100) // 10) + (((i % 1000) % 100) % 10)
            if res <= 10000:
                arr.append(res)
    arr.sort()
    arr1 = [i for i in range(1, 10001)]
    notSelf = [item for item in arr1 if item not in arr]
    for each in notSelf:
        print(each)

self_num()