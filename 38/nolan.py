import xml.etree.ElementTree as ET

# from OMDB
xmlstring = '''<?xml version="1.0" encoding="UTF-8"?>
<root response="True">
  <movie title="The Prestige" year="2006" rated="PG-13" released="20 Oct 2006" runtime="130 min" genre="Drama, Mystery, Sci-Fi" director="Christopher Nolan" />
  <movie title="The Dark Knight" year="2008" rated="PG-13" released="18 Jul 2008" runtime="152 min" genre="Action, Crime, Drama" director="Christopher Nolan" />
  <movie title="The Dark Knight Rises" year="2012" rated="PG-13" released="20 Jul 2012" runtime="164 min" genre="Action, Thriller" director="Christopher Nolan" />
  <movie title="Dunkirk" year="2017" rated="PG-13" released="21 Jul 2017" runtime="106 min" genre="Action, Drama, History" director="Christopher Nolan" />
  <movie title="Interstellar" year="2014" rated="PG-13" released="07 Nov 2014" runtime="169 min" genre="Adventure, Drama, Sci-Fi" director="Christopher Nolan"/>
</root>'''  # noqa E501

def _get_runtime(element):
    """Takes an ElementTree Element and returns its runtime parsed as an int
    assumes runtimes are all in format: 'int min'"""
    runtime_string = element.attrib['runtime']
    return int(runtime_string.split()[0])


def get_tree():
    """You probably want to use ET.fromstring"""
    return ET.fromstring(xmlstring)


def get_movies():
    """Call get_tree and retrieve all movie titles, return a list or generator"""
    tree = get_tree()
    return map(lambda movie: movie.get('title'), tree.findall('movie'))


def get_movie_longest_runtime():
    """Call get_tree again and return the movie with the longest runtime in minutes,
       for latter consider adding a _get_runtime helper"""
    tree = get_tree()
    longest_movie = sorted(tree.findall('movie'), key=_get_runtime, reverse=True)[0]
    return longest_movie.attrib['title']
