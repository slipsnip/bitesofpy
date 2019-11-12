import os
import re
import urllib.request
from operator import itemgetter
from collections import Counter


# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve('http://bit.ly/2zD8d8b', tempfile)

with open(tempfile) as f:
    content = f.read().lower()


# start coding

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    tags = Counter(re.findall(r'<category>(.+?)</category>', content))
    return sorted(tags.items(), key=itemgetter(1), reverse=True)[:n]
