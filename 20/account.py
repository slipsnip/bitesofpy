class Account:

    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)
        try:
            if self._managed:
                if self.balance < 0:
                    self._transactions.pop()
        except AttributeError:
            pass

    def __enter__(self):
        self._managed = True
        return self


    def __exit__(self, type, value, traceback):
        pass