# Сет (список штатов)
states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

# Хеш таблица (станций)
stations = {}
stations['kone'] = {'id', 'nv', 'ut'}
stations['ktwo'] = {'wa', 'id', 'mt'}
stations['kthree'] = {'or', 'nv', 'ca'}
stations['kfour'] = {'nv', 'ut'}
stations['kfive'] = {'ca', 'az'}


# Структура данных для хранения итогового набора станций
final_stations = set()

# Алгоритм

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)

