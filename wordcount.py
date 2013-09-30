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
        lower_word = word.lower().rstrip('\n.,?')
        number_of_times = wordcount.get(lower_word, 0)
        number_of_times += 1
        wordcount[lower_word] = number_of_times      
"""
for key, value in wordcount.iteritems():
    print key, value
"""

keys = wordcount.keys()

sorted_keys = sorted(keys)

print "Keys sorted alphabetically:"
for key in sorted_keys:
    print key, wordcount[key]

print "Keys sorted by frequency:"


values = wordcount.values()

sorted_values = sorted(values)

max_value = sorted_values[-1]

super_sorted_list = []
for i in range(1, max_value + 1):
    for key, value in wordcount.iteritems():
        if value == i:
            print key , value

