zakupy = {'Piekarnia':['bułka', 'chleb', 'drożdżowka', 'ciastko'], 'Warzywniak': ['pomidor', 'sałata', 'cukinia', 'cebula'], 'Apteka': ['etopiryna', 'krople do oczu']}

suma = 0
for key, value in zakupy.items():
    print(f'Idę do {key.title()} żeby kupić {[values.title() for values in value ]}')
    suma += len(value)
print(f'W sumie kupuję {suma} produktów.')   

print("******")
print("Miłego dnia i smacznej kawusi")