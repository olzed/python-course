users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptyList = []

print("Dave" in users) # true
print("Dave" in data) # true
print("Dave" in emptyList) # false

print(users[0])
print(users[-1]) # outputs last value in the list

print(users.index('Sara'))

print(users[0:2]) # range
print(users[1:]) # range from [1] to end of list
print(users[-3:-1])

print(len(data))

users.append('Elsa') # add Elsa to list
print(users)

users += ['Jason'] # short for VAR = VAR + new value
# ensure the syntax follows ['Value']
# as 'Value' it will be added like
# 'V', 'a', 'l', 'u', 'e'
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

# users.extend(data) # add an list to an list
# print(users)

users.insert(0, 'Bob') # adds Bob to position 0 of the list
print(users)

users[2:2] = ['Eddie', 'Alex'] # insert two values at the 2nd position
print(users)

users[1:3] = ['Robert', 'JPJ']
print(users)

users.remove('Bob')
print(users)

del users[0]
print(users)

data.clear() # delete all values in list
print(data)

users[1:2] = ['dave']
users.sort() # Sorted alphabetically, ['dave'] goes to the end of list
print(users)

users.sort(key=str.lower) # includes lowercase in sorting
print(users) # dave goes to position 0

nums = [4,42,78,1,5]
nums.reverse() # list in reverse order (begins with 5)
print(nums)

# nums.sort(reverse=True) # sort list in DESCENDING order
# print(nums)

print(sorted(nums, reverse=True)) # also sorts list in descending

numsCopy = nums.copy()
myNums = list(nums)
myCopy = nums[:]

print(numsCopy)
print(myNums)
myCopy.sort()
print(myCopy)
print(nums)

print(type(nums))

myList = list([1,"Neil", True])
print(myList)

# Tuples
# Like lists, data inside tuples does not change
# Data order does not change

myTuple = tuple(('Dave',42,True))

anotherTuple = (1,4,2,8,2,2)

print(myTuple)
print(type(myTuple))
print(type(anotherTuple))

newList = list(myTuple)
newList.append('Neil')
newTuple = tuple(newList)
print(newTuple)

(one, two, *hey) = anotherTuple
print(one) # holds the value '1'
print(two) # holds the value '4'
print(hey) # holds the value [2, 8] due to the asterisk

print(anotherTuple.count(2)) # counts the occurences of a value in a tuple
# in this instance it outputs 3