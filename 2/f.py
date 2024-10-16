from re import findall

file = open("input.txt", "r")
amount = int(file.readline())
text = file.read()
file.close()
words = map(lambda word: word.lower(), findall("[a-zA-Z]+", text))

word_occasions_count = dict()
for word in words:
    if word not in word_occasions_count.keys():
        word_occasions_count[word] = 1
    else:
        word_occasions_count[word] += 1

sorted_unique_words = sorted(sorted(word_occasions_count.keys()),
                      key = word_occasions_count.get,
                      reverse = True)

print(" ".join(sorted_unique_words[:amount]))