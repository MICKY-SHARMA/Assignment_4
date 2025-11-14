#TASK 1

try:
    # Try opening the file
    with open("sample.txt", "r") as file:
        print("File content:\n")
        # Print file content line by line
        for line in file:
            print(line.strip())
except FileNotFoundError:
    # Handle the error if file is missing
    print("Error: The file 'sample.txt' does not exist.")

    #TASK 2 

# Step 1: Take user input and write to a file
text = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text + "\n")

# Step 2: Append additional data
append_text = input("Enter text to append to the file: ")

with open("output.txt", "a") as file:
    file.write(append_text + "\n")

# Step 3: Read and display final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())

