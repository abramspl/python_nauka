def print_models(unprinted_designs, completed_models):
    """
    Symuluje wydruk poszczegulnych projektow, dopoki pozostal jakikolwiek
    projekt na liscie. Kazdy wydrukowany model zostaje przniesiony na
    liste comleted_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Wydruk modelu: {current_design}')
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Wyswietla wszystkie modele, ktore zostaly wydrukowane"""
    print('\nWydrukowane zostaly nastepujace modele:')
    for completed_model in completed_models:
        print(completed_model)