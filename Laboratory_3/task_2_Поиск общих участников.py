def find_common_participants(group_first, group_second, separator=','):  # TODO Напишите функцию find_common_participants, которая принимает 2 строки и третий аргумент, по умолчанию равный запятой
    list_first = group_first.split(separator)  #TODO делим первую строку на список подстрок, разделённых через каждое значение переменной separator (в данном случае ',')
    list_second = group_second.split(separator) #TODO делим вторую строку на список подстрок, разделённых через каждое значение переменной separator (в данном случае ',')
    common_participants = set(list_first).intersection(set(list_second)) #TODO представляем (изменяем тип для операции) списки как множества (чтобы функция intersection работала корректно) и находим их пересение, которое записываем в данную переменную
    common_participants_list = list(common_participants) #TODO переводим множество обратно в список, чтобы похже сделать сортировку
    common_participants_list.sort() #TODO сортируем в алфавитном порядке
    return common_participants_list #TODO возвращаем искомое значение и завершаем выполнение функции

participants_first_group = "Иванов|Петров|Сидоров" #TODO получаем значение - участников первой группы
participants_second_group = "Петров|Сидоров|Смирнов" #TODO получаем значение - участников второй группы

print(find_common_participants(participants_first_group, participants_second_group)) #TODO выводим результат функции для заданных переменных

# TODO Провеьте работу функции с разделителем отличным от запятой
#TODO при используемом разделителе функция выводит 0, если же значение переменной separator совпадает с используемым разделителем в строках, то функция вернёт корректный список общих участников