sentence = input("Enter a sentence: ")
words = sentence.split()  
word_frequency = {}

for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

print(word_frequency)
