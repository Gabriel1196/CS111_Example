# version 1.0.1

"""
Author: Gabriel Hernandez
Insitution: Big Bend Community College
Date: 11/17/2023

This program reads in a file containing a list of to-do items.
The items are read in to a dictionary of dictionaries.
The dictionary value is a dictionary, containing the value of the to-do item,
and the completion state of that item:
False if not completed, True if completed.
"""

import sys

def main():
    fileIn= open("listOfItems.txt")

    toDo = dict

    # loop through the libes in the file
    for line in fileIn:
        # create a list from the lines
        # delimiter: '. '
        # structure: item[0] is the number, key
        #            item[1] is the to do string
        #            toDo item will have a value of a dictionary
        #            False - to-do list item  has not been completed
        #            True - to-do list item has been completed
        item = line.split(". ")
        toDo[item[0]] = item[1], False}

    fileIn.close()


main()
