size_of_array = int(input("Enter the size of the array"))
array = []
for i in range(size_of_array):
    array.append(int(input()))
array.sort()
index = int(input("Enter the index"))
print(array[index-1])
