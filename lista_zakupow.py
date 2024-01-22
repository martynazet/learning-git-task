zakupy = {'Piekarnia':['bułka', 'chleb', 'drożdżowka'], 'Warzywniak': ['pomidor', 'sałata', 'cukinia']}

for key, value in zakupy.items():
    print(f'Idę do {key} żeby kupić {[values for values in value ]}')