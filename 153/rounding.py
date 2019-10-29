from decimal import (Decimal, Context, ROUND_UP, ROUND_DOWN, setcontext)
def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) ronud up, else round down.
       Return a new list of rounded values
    """
    WHOLE_NUM = Decimal(1)
    context = Context(rounding=ROUND_UP) if up else Context(rounding=ROUND_DOWN)
    setcontext(context)
    return [Decimal(num).quantize(WHOLE_NUM) for num in transactions]