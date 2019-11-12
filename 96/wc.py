import re
# imports for the nltk variant of wc
# from nltk.tokenize import (RegexpTokenizer, line_tokenize)
# import nltk.data


def wc(file_):
    with open(file_) as file_pointer:
        data = file_pointer.readlines()

    data = ''.join(data)
    breakpoint()
    character_regex = re.compile(r'[^\n]|\s')  # any single character or whitespace
    word_regex = re.compile(r'\w+?\b')  # one or more of anything not a space
    line_regex = re.compile(r'^.*\n')  # anything that ends in newline
    line_count = len(line_regex.findall(data))
    word_count = len(word_regex.findall(data))
    char_count = len(character_regex.findall(data))
    return f'{line_count} {word_count} {char_count} {file_}'

    
# First try to give myself practice using nltk, slow , took 3 seconds to
# process.  Not well suited for tokenizing
# def wc_nltk_variant(file_):
#     """Takes an absolute file path/name, calculates the number of
#        lines/words/chars, and returns a string of these numbers + file, e.g.:
#        3 12 60 /tmp/somefile
#        (both tabs and spaces are allowed as separator)"""
#     character_tokenizer = RegexpTokenizer(r'.|\s')
#     word_tokenizer = RegexpTokenizer(r'[^\s]+')
#     file_data = nltk.data.load('file:' + str(file_), format='text')
#     lines = line_tokenize(file_data, blanklines='keep')
#     words = word_tokenizer.tokenize(file_data)
#     characters = character_tokenizer.tokenize(file_data)
#     return f'{len(lines)} {len(words)} {len(characters)} {file_}'




if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))
