words = input("Text: ")
word_list = []
count = []
word_list = words.lower().split()
occurences = {}
word_length = []

for word in word_list:
    occurences[word] = occurences.get(word,0) + 1
    word_length.append(len(word))

for i in occurences:
    count.append(occurences[i])



sorted_occurences = dict(sorted((key,value) for (key,value) in occurences.items()))
word_length = sorted(word_length)
word_length.reverse()
longest_word = word_length[0]



for i in sorted_occurences:
        print("{:{}}: {}".format(i, longest_word,  sorted_occurences[i]))