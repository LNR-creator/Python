# Python

# Useful Shortcuts in Python

### 1. Swap Two Variables

```
a,b = b,a               # without using extra variable
```

### 2. Reverse A List
```
nums = [1,2,3,4,5]
print(nums[::-1])           # using slicing
```

### 3. Remove Duplicates
```
nums = [1,2,2,3,3,3]
unq = list(set(nums))           # by converting list to set
print(unq)                      # output : [1,2,3]
```

### 4. Get the Last Element

```
nums = [10,20,30,40,50]
last_ele = nums[-1]              # using negative indexing
print(last_ele)                  # output : 50
``` 

### 5. Flatten 2D List to 1D List

```
nums = [[1,2,3],[4,5,6],[7,8,9]]
flatten = [x for row in nums for x in row]
print(flatten)                                #output : [1,2,3,4,5,6,7,8,9]
```

### 6. First Non-Repeating Element
```
from collections import counter

nums = [1,1,2,2,3,3,5,6,6]
freq = count(nums)

for x in nums:
    if freq[x] == 1:
        print(x)
        break
```

### 7. Common Elements Btw two Lists
```
lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9,1,2]
common = list(set(lst1) & set(lst2))
print(common)                           # output : [1,2]
```

### 8. Merging Two Dictionaries

```
dt1 = {"name" : "Raj","age": 20}
dt2 = {"course": "Python"}

merged = {**dt1,**dt2}
print(merged)               # output :  {"name" : "Raj","age":20,"course": "Python"}
```

### 9. Filter Even Numbers
```
nums = [1,2,3,4,5,6]
even_nums = [x for x in nums if x%2 == 0]
print(even_nums)                            # output : [2,4,6]
```

### 10. Sort a List
```
# use sorted() or .sort()

nums = [4,5,6,2,8,2]
print(sorted(nums))             # for acsending order
print(nums.sort(reverse=True))  # for decending order
```

### 11. Convert String to Integers
```
input_str = "1 2 3 4 5"
nums = [map(int,input_str.split())]
print(nums)
```

### 12. Reverse a String
```
str = "Raju"
print(str[::-1])
```

### 13. Palindrome Check
```
s = "madam"
is_palindrome = s == s[::-1]
print(is_palindrome)            #   output : True
```

### 14. Get Maximum & Minimum
```
nums = [10,20,30,40,50]
print(max(nums))
print(min(nums))
```

### 15. Check All or Any Elements
```
nums = [1,2,3]
print(all(x > 0 for x in nums))       # output : True
print(all(x > 5 for x in nums))       # output : False
```

### Check if Two Strings are Anagram
```
a = "listen"
b = "silent"

print(sorted(a) == sorted(b))           # output : True
```