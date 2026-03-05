list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle_index = len(list_players) // 2
#TODO найти количество игроков в каждой команде, поделив количество игроков нацело пополам (индекс середины)

first_team = list_players[:middle_index]
#TODO определить игроков первой каоманды, записывая элементы, начиная с индекса [0] и заканчивая индексом [middle_index - 1]
second_team = list_players[middle_index:]
#TODO определить игроков второй каоманды, записывая элементы, начиная с индекса [middle_index] до конца

print(first_team)
print(second_team)
