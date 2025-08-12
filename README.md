task 1 :- 
# Create sample.txt with two lines
with open("sample.txt", "w") as f:
    f.write("This is a sample text file.\n")
    f.write("It contains multiple lines.\n")

# Read the file with error handling
try:
    print("Reading file content:")
    with open("sample.txt", "r") as f:
        for i, line in enumerate(f, start=1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

task 2 ;- 

# Step 1: Write data to output.txt
text_to_write = input("Enter text to write to the file: ")
with open("output.txt", "w") as f:
    f.write(text_to_write + "\n")
print("Data successfully written to output.txt.\n")

# Step 2: Append additional data
text_to_append = input("Enter additional text to append: ")
with open("output.txt", "a") as f:
    f.write(text_to_append + "\n")
print("Data successfully appended.\n")

# Step 3: Read and display final content
print("Final content of output.txt:")
with open("output.txt", "r") as f:
    print(f.read())
