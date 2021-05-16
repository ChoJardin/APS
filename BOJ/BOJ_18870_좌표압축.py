import sys

N = int(input())

nums= list(map(int, sys.stdin.readline().strip().split()))
sorted = sorted(list(set(nums[:])))
sorted_dict = {}
for idx, each in enumerate(sorted):
    sorted_dict[each] = idx

for num in nums:
    print(sorted_dict[num], end = ' ')