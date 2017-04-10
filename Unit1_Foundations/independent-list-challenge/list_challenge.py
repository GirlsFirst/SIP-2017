
from random import *

#Code below is the skeleton for a simple name generator.

#Create the list of words you want to choose from.
word_list = ["frank", "bean", "jean", "louis", "lisa", "pisa", "italy", "spaghetti"]

name = ""

for x in range(2):

    #Generates a random integer.
    x = randint(0, len(word_list)-1)
    name += word_list[x] + " "

print(name)
