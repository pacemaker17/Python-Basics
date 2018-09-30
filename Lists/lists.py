list1 = [1, 2, 3, "Ashpreet"]
print(list1)

# List of lists
list2 = [[1,2], [3,4]]
print(list2)

# Sorts the list and store in new list
numbers = [4,3,5,1,3,2,7]
print("Sorted list is :", sorted(numbers))

#Sorts the list in same list itself
numbers.sort()
print("Sort list is :", numbers)


#Slicing
print("Slicing: Print all numbers", numbers[:])
#Print from 0 to index 3
print(numbers[0:4])

# list[start : end : step-size]
#To print alternate numbers

print(numbers[::2])