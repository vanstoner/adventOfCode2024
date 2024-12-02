# Path to the input (maybe make this a command line arg in future)
file_path = 'day1-input.txt'  

# Create some arrays to store numbers from the file
array1 = []
array2 = []

# Process the file
with open(file_path, 'r') as file:
    for line in file:
        numbers = line.strip().split()  # tokenize
        if len(numbers) == 2:  # sanity check for a pair of numbers
            array1.append(float(numbers[0]))
            array2.append(float(numbers[1]))

# Sort the arrays
array1.sort()
array2.sort()

# Calculate the running total of differences
running_total = 0
differences = []

for i in range(len(array1)):
    difference = abs(array1[i] - array2[i]) 
    differences.append(difference)
    running_total += difference

# Print the results
print("Sorted Array 1:", array1)
print("Sorted Array 2:", array2)
print("Differences:", differences)
print("Running Total of Differences:", running_total)


# Part Two!
similarity_score = 0

for num in array1:
    count_in_array2 = array2.count(num)  # Count occurrences in the second array

    # Calculate a total similarity score by adding up each number in the left list 
    # after multiplying it by the number of times that number appears in the right list
    similarity_score += num * count_in_array2 

print("Sorted Array 1:", array1)
print("Sorted Array 2:", array2)
print("Differences:", differences)
print("Running Total of Differences:", running_total)
print("Similarity Score:", similarity_score)
