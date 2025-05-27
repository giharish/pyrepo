import re
fname = open('/Users/girishraja/Downloads/regex_sum_2190660.txt')
numlist = list()
for word in fname:
    word = word.rstrip()
    temp = (re.findall('[0-9]+', word))
    if len(temp) == 0: continue
    for items in temp:
        number = int(items)
        numlist.append(number)
print ('The Sum is: ', sum(numlist))
print ('The total numbers in list is', len(numlist))
