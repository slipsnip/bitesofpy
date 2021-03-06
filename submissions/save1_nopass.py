#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {
    letter: score
    for score, letters in scrabble_scores for letter in letters.split()
}

# start coding


def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY, 'r') as dictionary_file:
        dictionary = dictionary_file.readlines()
    return dictionary


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    score = 0
    for letter in list(word):
        if letter in LETTER_SCORES:
            score += LETTER_SCORES[letter]
    return score

def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    if (words == None):
        return None
    # dictionary of words and their associated score { word: score }
    scored_words = { word: calc_word_value(word) for word in words}
    # sort by largest score to lowest
    words_sorted_by_score = sorted(scored_words, key=lambda word_score: word_score[1])
    return words_sorted_by_score[0]