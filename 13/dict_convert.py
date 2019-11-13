from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

Blog = namedtuple('Blog', blog.keys())


def dict2nt(dict_):
    return Blog._make(blog.values())


def nt2json(nt):
    blog_dict = nt._asdict()
    blog_dict['started'] = blog_dict['started'].isoformat()
    return json.dumps(blog_dict)
