menus = {'Aamiainen': ['Kaurapuuro', 'Kahvi', 'Karpaloita' ],
         'Lounas': ['Kalastaa', 'Turkki', 'Perunat'],
         'Päivälinen': ['Manteli', 'Piirakka', 'Marjoja']}

for name, menu in menus.items():
    print(name, ':', menu)

henkilö = {'nimi': 'Ahti Hutamekki',
           'kaupunki': 'Tampere',
            'ikä': '36'}

print(henkilö.get('nimi'), 'on', henkilö.get('ikä'), 'vuotias')