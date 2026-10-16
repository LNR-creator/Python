# Find Common Elements btw two lists (Use set intersection)

nums1 = [1,2,3,4,5]
nums2 = [6,7,8,1,2]
common = list(set(nums1) & set(nums2))
print(common)