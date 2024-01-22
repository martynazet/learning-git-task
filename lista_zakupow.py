zakupy = {'Piekarnia':['bułka', 'chleb', 'drożdżowka'], 'Warzywniak': ['pomidor', 'sałata', 'cukinia']}

suma = 0
for key, value in zakupy.items():
    print(f'Idę do {key.title()} żeby kupić {[values.title() for values in value ]}')
    suma += len(value)
print(f'W sumie kupuję {suma} produktów.')   