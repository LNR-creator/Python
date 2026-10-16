# find the first Non-Repeating Element


# Using Counter
# Use Counter() for count frequency
from collections import Counter

nums = [1,1,2,2,3,3,3,4,4,5]
freq = Counter(nums)

for x in nums:
    if freq[x] == 1:
        print(x)
        break
