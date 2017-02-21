import csv
import string

f = open('cities.csv')

randomNums = f.read()
dataToSort = randomNums.split("\n")

length = len(dataToSort)


dataToSort = dataToSort[0:length-2]
length = len(dataToSort)

unsorted = True
hold = 0

while unsorted:

    i = 0                                           # set index to 0
    unsorted = False                                # set unsorted to false, so that you exit the while loop if you don't swap anything.

    for data in dataToSort[0:length]:                         # iterate through the list

        if i < length-1:

            if dataToSort[i] > dataToSort[i+1]:     # check each item with the item next to it, and swap if out of order.
                hold = dataToSort[i]
                dataToSort[i] = dataToSort[i+1]
                dataToSort[i+1] = hold
                unsorted = True                     # need to stay in while-loop

        i = i + 1                                   # increment index

print(dataToSort)
