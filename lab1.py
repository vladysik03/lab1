import json

file=open ('pokemon_full.json')
pokemon_string = file.read ()
#вывод 1 пункта
print ('Количество символов в файле:',len (pokemon_string))

count = 0
for symbol in pokemon_string:
    if symbol.isalnum ():
        count += 1
#вывод 2 пункта
print ('Количество символов в файле без пробелов и знаков препинания:',count)

pokemon_full_list = json.loads (pokemon_string)
max_lenght = 0
pokemon_name = ' '
for descr in pokemon_full_list:
    max_lenght = max (len (descr['description']), max_lenght)
    if len (descr['description']) == max_lenght:
        pokemon_name = descr['name']
#вывод 3 пункта
print ('Длина:', max_lenght, 'Покемон:', pokemon_name)
max_lenght = 0
max_ability = ' '
for abilities in pokemon_full_list:
    for ability in abilities['abilities']:
        max_lenght = max (len (ability.split ()), max_lenght)
        if max_lenght == len (ability.split ()):
            max_ability = ability
#вывод 4 пункта
print ('Умение: ', max_ability)
file.close ()
