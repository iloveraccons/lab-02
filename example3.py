with open('output.txt', 'w') as f:
    f.write("This is a new file.\n")
    f.write("It has two lines.\n")


# Copy all lines from sample.txt into copy.txt
with open('sample.txt', 'r') as src, open('copy.txt', 'w') as dst:
    for line in src:
        dst.write(line)
