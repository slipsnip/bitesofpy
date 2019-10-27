from collections import Counter
from operator import itemgetter

import requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    car_by_year = filter(lambda car: car.get('year') == year, data)
    new_cars = set([(car.get('automaker'), car.get('model'))
                    for car in car_by_year])
    counted = Counter([car[0] for car in new_cars])
    return max(counted.items(), key=itemgetter(1))[0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    filtered = filter(lambda car: car.get('automaker') == automaker and car.get('year') == year, data)
    return set([car.get('model') for car in filtered])
