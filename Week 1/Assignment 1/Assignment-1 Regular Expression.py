# Assignment Description:
# Finding Numbers in a Haystack
#
# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers
# in the file and compute the sum of the numbers.

import re

try:
    fileName = input("Enter the file Name: ")
    counter = 0
    valList=[]
    if len(fileName) < 1:
        fileName = "actual dataset"
        fileHandle = open(fileName)

## Approach 1 to find the sum:

    # for lines in fileHandle:
    #     # print(lines)
    #     for words in lines.split():
    #         # print(words)
    #         if words.isdigit():
    #             counter += int(words)
    #
    # print("Sum = ", counter)

## Approach 2 using the Regex:

    for lines in fileHandle:
        # valList.append(re.findall('[0-9]+', lines))
        valList = re.findall('[0-9]+', lines)
        for i in valList:
            counter += int(i)

    print(counter)

except Exception as e:
    print("Exception raised : ", e)
