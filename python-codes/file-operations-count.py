fname = input("Enter file name: ")
count = 0
fh = open(fname)
for line in fh:
    if line.startswith("From "):
        line.rstrip()
        line = line.split()
        print(line[1])
        count = count+1
print("There were", count, "lines in the file with From as the first word”)
