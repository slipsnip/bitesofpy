import os
import pytest
from movies import MovieDb
from copy import deepcopy
from collections import namedtuple

Movie = namedtuple('Movie', 'title year score_gt')

DB = os.path.join(os.getenv("TMP", "/tmp"), 'movies.db')
# https://www.imdb.com/list/ls055592025/
DATA = [
    ("The Godfather", 1972, 9.2),
    ("The Shawshank Redemption", 1994, 9.3),
    ("Schindler's List", 1993, 8.9),
    ("Raging Bull", 1980, 8.2),
    ("Casablanca", 1942, 8.5),
    ("Citizen Kane", 1941, 8.3),
    ("Gone with the Wind", 1939, 8.1),
    ("The Wizard of Oz", 1939, 8),
    ("One Flew Over the Cuckoo's Nest", 1975, 8.7),
    ("Lawrence of Arabia", 1962, 8.3),
]
TABLE = 'movies'

def remove_id_(query):
    return [record[1:] for record in query]

@pytest.fixture()
def db():
    # instantiate MovieDb class using above constants
    # do proper setup / teardown using MovieDb methods
    # https://docs.pytest.org/en/latest/fixture.html (hint: yield)
    movieDb = MovieDb(DB, DATA, TABLE)
    movieDb.init()
    yield movieDb
    movieDb.drop_table()
    del movieDb


# write tests for all MovieDb's query / add / delete
@pytest.mark.parametrize("title,year,score_gt", DATA)
def test_query(db, title, year, score_gt):
    by_title = list(filter(lambda movie: movie[0] == title, DATA))
    title = title if not "'" in title else title.replace("'", "''")
    assert remove_id_(db.query(title=title)) == by_title
    by_year = list(filter(lambda movie: movie[1] == year, DATA))
    assert remove_id_(db.query(year=year)) == by_year
    by_score = list(filter(lambda movie: movie[2] > score_gt, DATA))
    assert remove_id_(db.query(score_gt=score_gt)) == by_score

    
def test_add(db):
    title, year, score = ("Radio Flyer", 1992, 7.0)
    id = db.add(title, year, score)
    radio_flyer = db.query(title=title)
    assert radio_flyer[0][0] == id


    

def test_delete(db):
    data_lost = [
    ("The Godfather", 1972, 9.2),
    ("The Shawshank Redemption", 1994, 9.3),
    ("Schindler's List", 1993, 8.9),
    ("Raging Bull", 1980, 8.2),
    ("Casablanca", 1942, 8.5),
    ("Gone with the Wind", 1939, 8.1),
    ("The Wizard of Oz", 1939, 8),
    ("One Flew Over the Cuckoo's Nest", 1975, 8.7),
    ("Lawrence of Arabia", 1962, 8.3),
    ]
    id = db.query(title="Citizen Kane")[0][0]
    db.delete(id)
    assert db.query(title="Citizen Kane") == []

