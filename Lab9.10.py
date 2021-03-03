import csv
frequency = {}
filename= input()
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    line = next(csvreader)
    for word in line:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

for i in frequency:
    print(i, frequency[i])