from functools import wraps
known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    @wraps(func)
    def wrapper(*args, **argv):
        user = args[0]
        if user in known_users:
            if user in loggedin_users:
                return func(user, f'welcome back {user}')
            return func(user, f'please login')
        return func(user, 'please create an account')
    return wrapper


@login_required
def welcome(user, msg=''):
    '''Return a welcome message if logged in'''
    return msg
