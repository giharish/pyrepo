name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
tmp = list()
for line in handle:
    if line.startswith ('From '):
        line.rstrip()
        line = line.split()
        line = line[5]
        line = line.split(':')
        words = line[0]
        counts[words] = counts.get(words , 0) + 1
for k , v in (sorted(counts.items())):
    print (k , v)
