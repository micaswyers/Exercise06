
from sys import argv

script, filename = argv

filename = open(filename)



def print_alphabetically(dictionary):
    print "Keys sorted alphabetically:"
    keys = dictionary.keys()

    sorted_keys = sorted(keys)

    for key in sorted_keys:
        print key, dictionary[key]





def print_by_frequency(dictionary):
    print "Keys sorted by frequency:"
    values = dictionary.values()

    sorted_values = sorted(values)

    max_value = sorted_values[-1]


    for i in range(1, max_value + 1):
        for key, value in dictionary.iteritems():
            if value == i:
                print key , value







def print_frequency_alphabetically(dictionary):
    super_sorted_list = {}

    for key in dictionary:
        new_key = dictionary.get(key)

        if super_sorted_list.get(new_key):
            super_sorted_list[new_key].append(key)
        else:
            super_sorted_list[new_key] = []
            super_sorted_list[new_key].append(key)
 

    for each in super_sorted_list:
        super_sorted_list[each] = sorted(super_sorted_list[each])

    print "Keys sorted by frequency alphabetically:"
    
    keys = super_sorted_list.keys()

    sorted_keys = sorted(keys)

    for key in sorted_keys:
        for item in super_sorted_list[key]:
            print item, key




wordcount = {}


for line in filename:
    words = line.split(" ")
    
    for word in words:
        lower_word = word.lower().strip('\n.,?"--;$(\'[_*\r')
        number_of_times = wordcount.get(lower_word, 0)
        number_of_times += 1
        wordcount[lower_word] = number_of_times      

print_alphabetically(wordcount)
print_by_frequency(wordcount)
print_frequency_alphabetically(wordcount)
