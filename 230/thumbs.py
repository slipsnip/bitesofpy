THUMBS_UP, THUMBS_DOWN = '👍', '👎'


class Thumbs:
    def __mul__(self, rhs):
        count = rhs
        if count == 0:
            raise ValueError('Specify a number')
        thumb = THUMBS_UP if count > 0 else THUMBS_DOWN
        count = abs(count)
        return f'{thumb} ({count}x)' if count >=4 else thumb * count 
    
    def __rmul__(self, rhs):
        return self.__mul__(rhs)