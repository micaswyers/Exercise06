import sys

def normalize(text):
    text = text.replace("--", " ")
    word_list = text.lower().split()   #lowers, splits and puts words into a list
    
    clean_list=[]
    for word in word_list:
        word = word.strip("?.,_;\":!'-") #removes punctuation
        clean_list.append(word)

    return clean_list

def print_by_frequency(dictionary): #prints by frequency (high-low) (slow)
    max_frequency = max(dictionary.values())
    
    for i in range(1, max_frequency+1):
        for key, value in dictionary.iteritems():
            if value == max_frequency-(i-1):
                print key , value

def print_by_frequency2(dictionary): #prints by frequency, alphabetically
    for k in sorted(dictionary.iteritems(), cmp=comparator):
        print k[0], k[1]

def comparator(x,y):
    #x is (key, value)
    #y is (key, value)
    if x[1] > y[1]:
        return 1
    elif x[1] < y[1]:
        return -1
    else:
        return cmp(x[0], y[0])

def main():
    script, input_text = sys.argv

    open_file = open(input_text)
    input_text = open_file.read()
    open_file.close()

    token_list = normalize(input_text)
    
    wordcount = {}
    
    for token in token_list:
        wordcount[token] = wordcount.get(token, 0) + 1

    # prints out a list of every word, with its frequency: 
    # for word in wordcount: 
    #     print word, wordcount[word] 

    print_by_frequency2(wordcount)


    
main()

