def kanapka(*skladniki):
    print('Przygotowuje kanapke z wybranymi skladnikami:')
    for skladnik in skladniki:
        print(f'- {skladnik.upper()}')

kanapka('ser','czosnek')
kanapka('papryka')
kanapka('salami','pomidor','kurczak','oliwki')