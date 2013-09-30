
from sys import argv

script, filename = argv

filename = open(filename)

wordcount = {}

for line in filename:
    words = line.split(" ")
    
    for word in words:
        lower_word = word.lower().strip('\n.,?"--;$(\'[_*\r')
        number_of_times = wordcount.get(lower_word, 0)
        number_of_times += 1
        wordcount[lower_word] = number_of_times      



def print_alphabetically(dictionary):

    keys = dictionary.keys()

    sorted_keys = sorted(keys)

    for key in sorted_keys:
        print key, dictionary[key]

print "Keys sorted alphabetically:"
print_alphabetically(wordcount)


def print_by_frequency(dictionary):

    values = dictionary.values()

    sorted_values = sorted(values)

    max_value = sorted_values[-1]


    for i in range(1, max_value + 1):
        for key, value in dictionary.iteritems():
            if value == i:
                print key , value

print "Keys sorted by frequency:"
print_by_frequency(wordcount)


print "Keys sorted by frequency alphabetically:"


def print_frequency_alphabetically(dictionary):
    values = dictionary.values()
    super_sorted_list = {}

    for value in values:
        super_sorted_list[value] = []



    for key in dictionary:
        super_sorted_list[dictionary[key]].append(key)

    for each in super_sorted_list:
        super_sorted_list[each] = sorted(super_sorted_list[each])

    print_alphabetically(super_sorted_list)


print_frequency_alphabetically(wordcount)
