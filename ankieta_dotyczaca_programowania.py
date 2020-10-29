tekst = '\nWitaj w naszej ankiecie. Prosze o podanie odpowiedzi na pytanie.\n'
tekst += 'Dlaczego lubisz programowanie? (Wpisz "exit" aby zakonczyc)\n'
tekst += 'Twoja odp: '

while True:
    odp = input(tekst)

    if odp == 'exit':
        break
    else:
        print('Dziekuje za Twoja odpowiedz.')
        with open('ankieta.txt', 'a') as zapis:
            zapis.write(f'{odp}\n')