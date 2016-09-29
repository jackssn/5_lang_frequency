import os
import string
import operator
from collections import Counter
from pprint import pprint


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath,'r') as f:
        return f.read()


def get_most_frequent_words(text):
    words = [word.strip(string.punctuation) for word in text.split() if word.strip(string.punctuation)]
    counts = Counter(words)
    return sorted(counts.items(), key=operator.itemgetter(1), reverse=True)[:10]

if __name__ == '__main__':
    filepath = input('Type full path to file:\n')
    text = load_data(filepath)
    if text:
        pprint(get_most_frequent_words(text))
    else:
        print('File not found')
