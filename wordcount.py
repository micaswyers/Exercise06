import sys

def normalize(text):
    text = text.replace("--", " ")
    word_list = text.lower().split()   #lowers, splits and puts words into a list
    
    clean_list=[]
    for word in word_list:
        word = word.strip("?.,_;\":!'-")
        clean_list.append(word)

    return clean_list

def print_by_frequency(dictionary):
    max_frequency = max(dictionary.values())
    
    for i in range(1, max_frequency+1):
        for key, value in dictionary.iteritems():
            if value == max_frequency-(i-1):
                print key , value

def main():
    script, input_text = sys.argv

    open_file = open(input_text)
    input_text = open_file.read()
    open_file.close()

    token_list = normalize(input_text)
    
    wordcount = {}
    
    for token in token_list:
        wordcount[token] = wordcount.get(token, 0) + 1

    print_by_frequency(wordcount)


    
    # for word in wordcount:
    #     print word, wordcount[word]
main()

