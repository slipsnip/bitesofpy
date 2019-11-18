def split_words_and_quoted_text(text):
    """Split string text by space unless it is
       wrapped inside double quotes, returning a list
       of the elements.

       For example
       if text =
       'Should give "3 elements only"'

       the resulting list would be:
       ['Should', 'give', '3 elements only']
    """
    # Without using regex split
    # This method gives a pytest on my Ryzen 1700x CPU of
    # ============================== 1 passed in 9.87s =============================== 
    result = []
    tmp = ''
    inQuote = False

    for i, char in enumerate(text):
        if char == r'"':
            if inQuote:
                inQuote = False
                result.append(tmp)
                tmp = ''
                continue
            else:
                inQuote = True
                continue
        if inQuote or char != ' ':
            tmp += char
            if i != len(text) - 1:
                continue
            else:
                result.append(tmp)
                break
        if tmp != '':
            result.append(tmp)
            tmp = ''
    return result