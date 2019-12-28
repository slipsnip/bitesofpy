from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join(
    os.getenv("TMP", "/tmp"),
    'course_timings'
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/course_timings',
    COURSE_TIMES
)

"""
In this Bite you read in a text file with course times (MM:SS) per video.

You extract these and calculate the total course duration in HH:MM:SS.

See the docstrings and tests for more details.

Have fun and we hope you learn a thing or two.

Trivia: in honor of our Code Challenges Pilot: this was the exercise we used to test the waters when we started out :)
"""


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    with open(COURSE_TIMES) as course_times_fd:
        course_times = course_times_fd.read()
    return re.findall(r'(?<=\()\d+:\d+(?=\))', course_times)


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    total = sum([int(time) if index % 2 != 0 else int(
        time) * 60 for t in timestamps for index, time in enumerate(t.split(':'))])
    hours, minutes = divmod(total, 60 * 60)
    minutes, seconds = divmod(minutes, 60)
    return f'{hours:02}:{minutes:02}:{seconds:02}'
