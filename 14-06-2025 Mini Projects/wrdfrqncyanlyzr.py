
# Word Frequency Analyzer

def word_frequency_analyzer(text):
    text = text.lower()

    word_list = text.split()
    print("\nList of words:", word_list)

    word_freq = {}

    for word in word_list:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    print("\nWord Frequencies:")
    for word in sorted(word_freq, key=word_freq.get, reverse=True):
        print(f"{word}: {word_freq[word]}")

input_text = input("Enter a paragraph:")
word_frequency_analyzer(input_text)