word_occurrence = {}
text = input("Text: ")
words = text.split()
for word in words:
    if word in word_occurrence:
        word_occurrence[word] += 1
    else:
        word_occurrence[word] = 1
words = list(word_occurrence.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {} ".format(word, max_length, word_occurrence[word]))
