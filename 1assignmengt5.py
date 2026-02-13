
'''
filename = "sample.txt"

# Step 1: Write to the file
with open(filename, "w") as file:
    file.write("This is a sample text file.\n")
    file.write("It contains multiple lines.\n")

# Step 2: Read from the file
with open(filename, "r") as file:
    print("Reading file content:")
    for i, line in enumerate(file, start=1):
        print(f"Line {i}: {line.strip()}")

'''



try:

    with open("sample.txt", "r") as file:
        print("Reading file content:")
        for i, line in enumerate(file, start=1):
         print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")