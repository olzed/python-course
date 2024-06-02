#def squared(num): return num * num
squared = lambda num : num * num

# 4
print(squared(2))

# def addTwo(num): return num + 2
# 14
addTwo = lambda num : num + 2
print(addTwo(12))

def sum_total(a, b): return a + b
sum_total = lambda a, b : a + b

# 18
print(sum_total(10, 8))

############

def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7)) # 17
print(addTwenty(7)) # 27

##########################

# higher order functions

numbers = [3, 7, 12, 18, 20, 21]

# MUCH more efficient than a loop
squared_nums = map(lambda num : num * num, numbers)

print(list(squared_nums))

##############################

# filter
# filters anything that wasn't true from the function

# [3, 7, 21]
odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

################################

from functools import reduce

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers, 10)) # sum of the numbers plus 10

# CHARACTER COUNT

names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt']

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)

print(char_count)