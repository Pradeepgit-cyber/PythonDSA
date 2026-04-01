# Replace characters
p = 'aaaa'
print(p.replace('a', 'b', 2))
# p = 'aaaa'
# old = 'a'
# new = 'b'
# n = 2
reversed_p = p[::-1]
reversed_replaced = reversed_p.replace('a', 'b', 2)
p_replaced = reversed_replaced[::-1]
print(p_replaced)

# How to print list without loop in python
lst = [12,33,44,55]
print(lst)
print(*lst, sep="\n")

# Find the output
p = {True:  "A", 1:  "B", False:  "C", 0:  "D"}
print(p)
d = {}
d[1] = "A"
d[True] = "B"
print(d)
a, b = "ab"
b, c = "cd"
print(a, b, c)

# print comman values in two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
comman = [x for x in list1 if x in list2]
print(comman)













# revesre a string
p = "paradeep"
print(p[::-1])

# check pallindrome
if p == p[::-1]:
    print("Its pallindrome")
else:
    print("Its not pallindrome")

# find largest number in list
numbers = [1, 2, 3, 4, 19, 6, 7, 8, 9, 20]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("largest number is : ", largest)
print(max(numbers))

# Second Largest Element
nums = [20,30,25,50,10]
nums = list(set(nums))
nums.sort()
print(nums[-2])


# split to convert string into list
text = "p k b"
reverse_text = "".join(text.split()[::-1])
print(reverse_text)

# Count each character frequency in a string.
s = 'seleniium'
d = {}
for char in s:
    if char in d:
        d[char] += 1
    else:
        d[char] = 1
print(d)

# Find duplicates in a list.
list = [1, 2, 3, 1, 4, 5, 2, 3]
duplicates = set()
seen = set()
for i in list:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)
print(duplicates)

# Swap Two Numbers
a = 10
b = 5

a, b = b, a
print(a, b)

# write a function to add two numbers
def add(a, b):
    return a + b
print(add(2, 3))


# Prime Number Check
num = 7
for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

# Find Missing Number
nums = [1,2,3,4,5,6,7,8,10]
n = 10
expected = n * (n + 1) // 2
actual = sum(nums)
print(expected - actual)


# Class & Object

class Car:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

c = Car("Audi")
c.show()