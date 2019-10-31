from collections import defaultdict
from operator import itemgetter
from itertools import groupby

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    people = [tuple(record.split(',')[::-1]) for record in data.splitlines()[1:] if record.strip()]
    countries = defaultdict(list)
    for country_code, first_name, last_name in people:
        countries[country_code].append(f'{first_name} {last_name}')
    return countries
    
