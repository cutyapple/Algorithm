nums = 1
o2nine = [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0, 0]
for i in range(3):
    nums *= int(input())
strs = list(str(nums))
for i in range(len(strs)):
    o2nine[int(strs[i])]+=1
for i in range(10):
    print(o2nine[i])