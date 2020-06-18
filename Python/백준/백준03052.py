results = []
for i in range(10):
    nums = int(input())
    if nums%42 not in results:
        results.append(nums%42)

print(results.__len__())