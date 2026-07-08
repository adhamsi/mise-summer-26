total = 49

# "w" opens for writing -- erases any existing content
with open("out.txt", "w") as f:
    f.write("Results\n")
    f.write("total: ")
    f.write(str(total) + "\n")

# "a" appends without erasing
with open("out.txt", "a") as f:
    f.write("done\n")
