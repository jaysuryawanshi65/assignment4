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


