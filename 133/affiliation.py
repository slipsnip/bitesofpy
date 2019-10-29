def generate_affiliation_link(url):
    parts = url.split('/')
    return 'http://www.amazon.com/dp/{5}/?tag=pyb0f-20'.format(*parts)
    