my_list = [1,2,3,4,5,5,3,2]
print(my_list)

# Append and Set examples
my_list.append(6)
print(my_list)
unique = set(my_list)
print(unique)
# Count and Index examples
print(my_list.count(3))
print(my_list[1])
print(my_list[-1])

# Remove example
nums = [1, 2, 3, 4, 5]
print(nums.remove(3))
print(nums)

for i in nums:
    print(i)

#length example
print(len(my_list))

#replacing element
my_list[1] = 100
print(my_list)


if 10 in my_list:
    print("Found 10")

else:
    print("10 not found")

#slincing example
print("Slicing examples:")
print(my_list[1:4])

#reverse example

print(my_list[::-1])