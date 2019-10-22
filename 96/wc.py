from nltk.tokenize import (RegexpTokenizer, line_tokenize)
import nltk.data

def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    character_tokenizer = RegexpTokenizer(r'.|\s')
    word_tokenizer = RegexpTokenizer(r'[^\s]+')
    file_data = nltk.data.load('file:' + str(file_), format='text')
    lines = line_tokenize(file_data, blanklines='keep')
    words = word_tokenizer.tokenize(file_data)
    characters = character_tokenizer.tokenize(file_data)
    return f'{len(lines)} {len(words)} {len(characters)} {file_}'




if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))
