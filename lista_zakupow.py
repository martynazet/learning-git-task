zakupy = {'Piekarnia':['bułka', 'chleb', 'drożdżowka'], 'Warzywniak': ['pomidor', 'sałata', 'cukinia']}

for key, value in zakupy.items():
    print(f'Idę do {key.title()} żeby kupić {[values.title() for values in value ]}')