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
