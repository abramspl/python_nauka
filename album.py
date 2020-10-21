def make_album(artysta, album):
    zespol = {'ARTYSTA / ZESPOL': artysta, 'ALBUM': album}
    return  zespol

artysta1 = make_album('oldfield','dzwony rurowe')
artysta2 = make_album('slawomir','rock-polo')
artysta3 = make_album('zenek','hity lata')

print(artysta1)
print(artysta2)
print(artysta3)

# wersja z trzecim parametrem i wartoscia "None"

def make_album(artysta, album, licz_utworow=None):
    zespol = {'ARTYSTA / ZESPOL': artysta, 'ALBUM': album}
    if licz_utworow:
        zespol['LICZ_UTWOROW'] = licz_utworow
    return  zespol

artysta1 = make_album('oldfield','dzwony rurowe',15)
artysta2 = make_album('slawomir','rock-polo')
artysta3 = make_album('zenek','hity lata',19)

print(artysta1)
print(artysta2)
print(artysta3)