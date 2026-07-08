# Read the whole file at once
with open("notes.txt") as f:
    text = f.read()

print(text)

# Read line by line (usually better for large files)
with open("notes.txt") as f:
    for line in f:
        print(line.strip())
