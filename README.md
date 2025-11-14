🐍 Python File Handling Tasks
📝 Overview

This project demonstrates the basics of file handling in Python, including reading, writing, appending, and handling errors safely.
Through these tasks.

📘 Task 1: Read a File and Handle Errors
Problem Statement

Write a Python program that:

Opens and reads a text file named sample.txt

Prints its content line by line

Handles errors gracefully if the file does not exist

Sample Code
try:
    with open("sample.txt", "r") as file:
        print("File content:\n")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

Expected Output
✔ If the file exists:
File content:

Hello World
This is a sample file
Python file handling example

❌ If the file does not exist:
Error: The file 'sample.txt' does not exist.

📘 Task 2: Write and Append Data to a File
Problem Statement

Write a Python program that:

Takes user input and writes it to output.txt

Appends additional text to the same file

Reads and displays the final content

Sample Code
text = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text + "\n")

append_text = input("Enter text to append to the file: ")

with open("output.txt", "a") as file:
    file.write(append_text + "\n")

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())

Expected Output
Enter text to write to the file: Hello World
Enter text to append to the file: This is appended text

Final content of output.txt:
Hello World
This is appended text

🧠 Concepts Covered

File reading (r mode)

File writing (w mode)

File appending (a mode)

Error handling (try-except)

Using context managers (with open)
