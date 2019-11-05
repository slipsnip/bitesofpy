import requests
from bs4 import BeautifulSoup
from functools import partial
from operator import itemgetter
import re

cached_so_url = 'https://bit.ly/2IMrXdp'


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    response = requests.get(cached_so_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    question_summarys = soup.find_all(class_='question-summary')
    questions = []
    for summary in question_summarys:
        vote_str = summary.find(class_='vote-count-post').string
        question = summary.find(class_='question-hyperlink').string
        views = summary.find(class_='views').string.strip()
        questions.append((question, int(vote_str), views))
    questions = [(question[0], question[1]) for question in questions if re.search(r'(\d)+(?=m)', question[-1])] 
    return sorted(questions, key=itemgetter(1), reverse=True)

