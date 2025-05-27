name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith ("From "):
        line.rstrip()
        line = line.split(' ')
        words = line[1]
        counts[words] = counts.get(words, 0) + 1
maxcount =  None
maxword = None
for word, count in counts.items():
    if maxcount is None or count > maxcount:
        maxword = word
        maxcount = count
print (maxword, maxcount)
