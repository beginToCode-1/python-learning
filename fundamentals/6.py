import os

test_file = "test.txt"

# Check if the file exists
print(os.path.exists(test_file))  # True if the file exists

# Open the file in read mode
with open(test_file, "r") as f:
    for line in f:
        print(line.strip())  # remove extra spaces and newline
