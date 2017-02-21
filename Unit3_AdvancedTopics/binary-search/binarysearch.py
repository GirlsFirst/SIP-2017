import csv
import string
import math

f = open('cities.csv')

randomNums = f.read()
citiesToSort = randomNums.split("\n")

length = len(citiesToSort)


# Sort Data
unsorted = True
hold = 0

while unsorted:
    i = 0                                           # set index to 0
    unsorted = False                                # set unsorted to false, so that you exit the while loop if you don't swap anything.
    for city in citiesToSort[0:length]:                         # iterate through the list
        if i < length-1:
            if citiesToSort[i] > citiesToSort[i+1]:     # check each item with the item next to it, and swap if out of order.
                hold = citiesToSort[i]
                citiesToSort[i] = citiesToSort[i+1]
                citiesToSort[i+1] = hold
                unsorted = True                     # need to stay in while-loop
        i = i + 1                                   # increment index


# Searhc Data
length = len(citiesToSort)
searchKey = input('What city are you looking for?:  ')

notFound = True
first = 0
last = len(citiesToSort)-1

while first<=last and notFound:

    index = int((first+last)/2)
    print(index)

    if searchKey == citiesToSort[index]:
        notFound = False
        print("We found your city!")

    else:

        if searchKey < citiesToSort[index]:
            last = index-1
        else:
            first = index+1

if notFound:
    print("Your city isn't here!")
