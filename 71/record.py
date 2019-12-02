class RecordScore(object):
    """Class to track a game's maximum score"""
    def __call__(self, score):
        try:
            if score > self._top_score:
                self._top_score = score
        except AttributeError:
            self._top_score = score
        finally:
            return self._top_score
