import os

# rawx - read, append, write, create

f = open("names.txt", "r")
# print(f.read())
# print(f.read(4))
# print(f.readline())
# print(f.readline())

for line in f:
    print(line)
    
f.close()

try:
    f = open("name_list.txt")
    print(f.read())
except:
    print("File doesn't exist.")
finally:
    f.close()
    
# Append - creates file if it doesn't exist
f = open("names.txt", "a")
f.write("\nNeil")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# write (overwrite)
f = open("context.txt", "w")
f.write("I deleted all of the context")
f.close()


# Opens a file for writing, creates file if it does not exist
f = open("name_lists.txt", "w")
f.close()

# Creates specified file, returns error if file exists

if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()
    
    
# delete a file
# avoid error if doesn't exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("File does not exist.")
    
with open("more_names.txt") as f:
    content = f.read()
    
with open("names.txt", "w") as f:
    f.write(content)