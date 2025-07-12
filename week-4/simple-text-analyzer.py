"""
This module provides simple text analysis functions.

What this program will do:
1. Count the number of words in a text.
2. Count the number of charactor in a text.
3. Count the number of sentences in a text.
4. Return a dictionary of vowel and its counts in a text.
5. Return a dictionary of word and its counts in a text.

How to use:
1. Run the program using 'python3 week-4/simple-text-analyzer.py' command.
2. Enter a text.
3. The program will display the results.
"""


# Count the number of words in a text.
def count_words(text):
    return len(text.split())

# Count the number of charactor in a text
def count_character(text, includeSpace=True):
    if includeSpace:
        return len(text)
    else:
        return len(text.replace(" ", ""));

# Count the number of sentences in a text
def count_sentence(text):
    sentence_endings = '.?!'
    count = 0

    for char in text:
        if char in sentence_endings:
            count += 1
    
    return count

# Return a dictionary of vowel and its counts in a text
def get_vowel_counts(text):
    vowels = "aeiou"
    vowels_dics = {}

    for char in text:
        if char.lower() in vowels:
            vowels_dics[char] = vowels_dics.get(char, 0) + 1

    return vowels_dics

# Return a dictionary of word and its counts in a text
def get_word_counts(text):
    word_dics = {}

    for char in text:
        word_dics[char] = word_dics.get(char, 0) + 1

    return word_dics;

# Analyze the text
def analyze_text(text, *args, **kwargs):
    results = {}

    if "words" in args:
        results["words"] = count_words(text)
    if "characters" in args:
        includeSpace = kwargs.get("includeSpace", True)
        results["characters"] = count_character(text, includeSpace)
    if "sentences" in args:
        results["sentences"] = count_sentence(text)
    if "vowels" in args:
        results["vowels"] = get_vowel_counts(text)
    if "word_counts" in args:
        results["words"] = get_word_counts(text);

    return results

# Main
def main():
    text = input("Enter a text: ");

    print(analyze_text(text, "words", "characters", "sentences", "vowels", "word_counts"));


main()