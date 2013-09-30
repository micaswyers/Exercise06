"""
open a file from the command line
read a line of the file
create a dictionary that makes a key of each new, space-separated word in the text file
for every occurence of the key in the text file, add one to the corresponding value
print dictionary contents to the screen
"""

from sys import argv

script, filename = argv

filename = open(filename)

wordcount = {}

for line in filename:
    words = line.split(" ")
    
    for word in words:
        number_of_times = wordcount.get(word, 0)
        number_of_times += 1
        wordcount[word] = number_of_times      

for key, value in wordcount.iteritems():
    print key, value

