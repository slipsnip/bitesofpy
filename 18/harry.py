import os
import urllib.request
from collections import Counter
from typing import List

# data provided
stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)


def parse_word_(word: str) -> str:
    return ''.join(letter.lower() for letter in word if letter.isalnum())


def is_word_(word: str, stop_words: List[str]) -> bool:
    word = parse_word_(word.lower())
    return word not in stop_words and word != ''


def get_harry_most_common_word():
    words = []
    stop_words = []
    with open(stopwords_file) as stop_words_fd:
        stop_words = stop_words_fd.read().split('\n')
        stop_words = [parse_word_(word) for word in stop_words]
        with open(harry_text) as harry_potter:
            for line in harry_potter:
                line = line.strip().split()
                line = [parse_word_(
                    word) for word in line if is_word_(word, stop_words)]
                words.extend(line)
    return Counter(words).most_common(1)[0]
