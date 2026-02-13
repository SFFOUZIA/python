# Step 1: Take user input and write to file
user_input = input("Enter text to write into the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")

print("Data succesfully written to output.txt.")

# Step 2: Append additional data
append_input = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(append_input + "\n")

print("Data successfully appended.")

# Step 3: Read and display final content
print("\nFinal content of output.txt:")

with open("output.txt", "r") as file:
    content = file.read()
    print(content)
