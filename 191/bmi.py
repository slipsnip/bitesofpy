from operator import itemgetter
from functools import partial
import csv


data = """Luke Skywalker,172,77
          C-3PO,167,75
          R2-D2,96,32
          Darth Vader,202,136
          Leia Organa,150,49
          Owen Lars,178,120
          Beru Whitesun lars,165,75
          R5-D4,97,32
          Biggs Darklighter,183,84
          Obi-Wan Kenobi,182,77
          Anakin Skywalker,188,84
          Chewbacca,228,112
          Han Solo,180,80
          Greedo,173,74
          Jek Tono Porkins,180,110
          Yoda,66,17
          Palpatine,170,75
          Boba Fett,183,78.2
          IG-88,200,140
          Bossk,190,113
"""

def calculate_bmi(mass, height, *, rnd=False, ndigits=2):
    """Return the BMI as a float calculated from mass and height

    :param mass: Body mass of person to be calculated
    :type mass: int
    :param height: Height of person
    :type height: int
    :param rnd: Bool indicating weather to round result, default=False
    :type rnd: bool
    :param ndigits: Number of digits percison after decimal, default=2
    :type ndigits: int
    :return: BMI as float
    :rtype: float
    """
    bmi = float(mass) / ((int(height) / 100) ** 2) 
    return bmi if not rnd else round(bmi, ndigits=ndigits) 


def person_max_bmi(data=data):
    """Return (name, BMI float) of the character in data that
       has the highest BMI (rounded on 2 decimals)"""
    rounded_bmi = partial(calculate_bmi, rnd=True)
    data = [line.strip() for line in data.splitlines() if line.strip() != '']
    people = csv.DictReader(data, fieldnames='name height mass'.split())
    bmi_stats = [(name, rounded_bmi(mass, height)) for name, height, mass in [person.values() for person in people]]
    return max(bmi_stats, key=itemgetter(1))
