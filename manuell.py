#https://docs.python.org/3/library/csv.html#
#https://stackoverflow.com/questions/4710067/how-to-delete-a-specific-line-in-a-text-file-using-python

import csv

Date = []
Open = []
Close = []

#Les av de tre kolonnene vi trenger for å beregne optimal handel
index = 0
with open("NVDA.csv", newline="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",")
    if(index == 0):
        next(spamreader)
    for row in spamreader:
        Date.append(row[0])
        Open.append(float(row[2]))
        Close.append(float(row[5]))

initialInvestment = 100

Value = []
for i in range(len(Date)):
    Change = (Close[i] - Open[i]) / Open[i] + 1
    if Change > 1:
        if(i > 0):
            Value.append(Value[i-1] * Change)
        else:
            Value.append(initialInvestment)
    else:
        if(i>0):
            Value.append(Value[i-1])
        else:
            Value.append(initialInvestment)

print(Value[-1])

