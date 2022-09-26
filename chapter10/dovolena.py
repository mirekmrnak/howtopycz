def navrat():
    week = [
        'Pondeli',
        'Utery',
        'Streda',
        'Ctvrtek',
        'Patek',
        'Sobota',
        'Nedele',
    ]
    den = int(input('Den odjezdu: '))
    delka = int(input('Délka pobytu: '))
    back = den + (delka % 7)
    if back > 6:
        back -= 7
        
    print(f'Vrátíš se ve {week[back]}')

navrat()