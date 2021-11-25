import json
file=open ('pokemon_full.json')
file_first = file.read()
#вывод 1 пункта
print("Количество символов в файле:",len(file_first))

count = 0
for i in file_first:
    if i.isalnum() == True:
        count += 1
#вывод 2 пункта
print("Количество символов в файле без пробелов и знаков препинания:",count)

pokemon_full_massive = json.loads(file1)
max_dlina = 0
pokemon_name = ' '
for descr in pokemon_full_massive:
    max_dlina = max(len(descr['description']),max_dlina)
    if len(descr['description']) == max_dlina:
        pokemon_name = descr['name']
#вывод 3 пункта
print("Длина:", max_dlina, "Покемон:", pokemon_name)

max_dlina = 0
max_ability = ' '
for abilities in pokemon_full_massive:
    for ability in abilities['abilities']:
        max_dlina = max(len(ability.split()),max_dlina)
        if max_dlina == len(ability.split()):
            max_ability = ability
#вывод 4 пункта
print("Умение: ", max_ability)
file.close()
