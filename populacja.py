def miasto_funkcja(miasto,panstwo,populacja=''):
    if populacja:
        dane = f'{miasto}, {panstwo} - populacja {populacja}.'
    else:
        dane = f'{miasto}, {panstwo}.'
    return dane.title()