def miasta_panstwa(miasto, panstwo):
    tekst = f'{miasto}, {panstwo}'
    return tekst.title()

miasto1 = miasta_panstwa('warszawa','polska')
miasto2 = miasta_panstwa('berlin','niemcy')
miasto3 = miasta_panstwa('moskwa','rosja')

print(miasto1)
print(miasto2)
print(miasto3)