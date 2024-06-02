# Dictionaries

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items in dictionaries
print(band["vocals"])
print(band.get("guitar"))

# List all keys
print(band.keys())

# list all values
print(band.values())

# list of key/values pairs as Tuples
print(band.items())

# verify key exists
print("guitar" in band) # True
print("triangle" in band) # False

# Change values
band["vocals"] = "Coverdale" # Plant -> Coverdalee
band.update({"bass": "JPJ"}) # Add new key value
print(band)

# remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) # removes last key pair that was added (Tuple)
print(band)

# Delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2 # deletes entire dictionary

# Copy dictionaries
# band2 = band # Creates a reference - referring to same memory location/same dictionary
# print("Bad copy!")
# print(band)
# print(band2)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy() # Does not create a reference - creates its own dictionary
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

# Or use the dict() constructor function
band3 = dict(band)
print("Good copy")
print(band3)

# Nested dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"]) # Plant

# Sets

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicate allowed
nums = {1, 2, 2, 3}
print(nums) # outputs {1, 2, 3}

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a set
print(2 in nums)

# but you cannot refer to an element in the set with an index position

# Add new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)

# You can use update() with lists, tuples, dictionaries

# Merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

myNewSet = one.union(two)
print(myNewSet)

# keep only duplicatees
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# Keep everything except duplicates

one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)

print(one.issubset(two)) # tests whether every element in one set is in the other
print(one.issuperset(two)) # tests whether every element in another set (two) is in the other (one)