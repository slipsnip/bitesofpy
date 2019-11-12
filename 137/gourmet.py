#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""

from collections import (Counter, defaultdict)
from enum import Enum
from operator import itemgetter
from itertools import (groupby, chain)

CHEESES = [
    "Red Leicester",
    "Tilsit",
    "Caerphilly",
    "Bel Paese",
    "Red Windsor",
    "Stilton",
    "Emmental",
    "Gruyère",
    "Norwegian Jarlsberg",
    "Liptauer",
    "Lancashire",
    "White Stilton",
    "Danish Blue",
    "Double Gloucester",
    "Cheshire",
    "Dorset Blue Vinney",
    "Brie",
    "Roquefort",
    "Pont l'Evêque",
    "Port Salut",
    "Savoyard",
    "Saint-Paulin",
    "Carré de l'Est",
    "Bresse-Bleu",
    "Boursin",
    "Camembert",
    "Gouda",
    "Edam",
    "Caithness",
    "Smoked Austrian",
    "Japanese Sage Derby",
    "Wensleydale",
    "Greek Feta",
    "Gorgonzola",
    "Parmesan",
    "Mozzarella",
    "Pipo Crème",
    "Danish Fynbo",
    "Czech sheep's milk",
    "Venezuelan Beaver Cheese",
    "Cheddar",
    "Ilchester",
    "Limburger",
]

RED_WINES = [
    "Châteauneuf-du-Pape",  # 95% of production is red
    "Syrah",
    "Merlot",
    "Cabernet sauvignon",
    "Malbec",
    "Pinot noir",
    "Zinfandel",
    "Sangiovese",
    "Barbera",
    "Barolo",
    "Rioja",
    "Garnacha",
]

WHITE_WINES = [
    "Chardonnay",
    "Sauvignon blanc",
    "Semillon",
    "Moscato",
    "Pinot grigio",
    "Gewürztraminer",
    "Riesling",
]

SPARKLING_WINES = [
    "Cava",
    "Champagne",
    "Crémant d’Alsace",
    "Moscato d’Asti",
    "Prosecco",
    "Franciacorta",
    "Lambrusco",
]

class Wines(Enum):
    RED = RED_WINES
    WHITE = WHITE_WINES
    SPARKLING = SPARKLING_WINES

def wine_cheese_simularity(wine: str, cheese: str) -> int:
    sum_intersect = sum(score for letter, score in Counter(wine).items() if letter in Counter(cheese))
    length_difference = abs(len(wine) - len(cheese))
    return sum_intersect / 1 + pow(length_difference, 2)

def best_match_per_wine(wine_type="all", get_max=True):
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """
    wines = Wines[wine_type.upper()].value if wine_type != 'all' else RED_WINES + WHITE_WINES + SPARKLING_WINES
    scored_pairs = [(wine, cheese, wine_cheese_simularity(wine, cheese)) for wine in wines for cheese in CHEESES]
    return max(scored_pairs, key=itemgetter(2)) if get_max else scored_pairs

    



def match_wine_5cheeses():
    """  pairs all types of wines with cheeses ; returns a sorted list of tuples,
    where each tuple contains: wine, list of 5 best matching cheeses.
    List of cheeses is sorted by score descending then alphabetically ascending.
    e.g: [
    ('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer']),
    ...
    ...
    ('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
    ]
    """
    best_of = defaultdict(str)
    for wine, pairs in groupby(best_match_per_wine(get_max=False), itemgetter(0)):
        best_of[wine] = [pair[1] for pair in sorted(pairs, key=itemgetter(2), reverse=True)][:5]

    return [(wine, best_of[wine]) for wine in best_of.keys()]
    
