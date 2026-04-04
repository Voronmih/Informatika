import csv     #TODO Импорт модуля csv для чтения и записи файлов в формате CSV
import json     #TODO Импорт модуля json для преобразования данных в формат JSON и обратно

INPUT_FILENAME = "input.csv"    #TODO имя входного CSV-файла
OUTPUT_FILENAME = "output.json" #TODO имя выходного JSON-файла

def task() -> None: #TODO задаём функцию task, которая не возвращает значение
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file: #TODO открываем CSV-файл на чтение в режиме текста с кодировкой UTF-8
        reader = csv.DictReader(csv_file) #TODO создаём объект DictReader, который читает CSV и использует первую строку как заголовки столбцов
        data = list(reader) #TODO преобразуем reader в список словарей

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file: #TODO открываем JSON-файл на запись в режиме текста с кодировкой UTF-8
        json.dump(data, json_file, indent=4, ensure_ascii=False) #TODO сериализуем список data в JSON и записываем в файл
if __name__ == '__main__': #TODO проверяем, что скрипт выполняется как основная программа
    task()  #TODO вызов функции

    #TODO вывод содержимого полученного JSON-файла для проверки
    with open(OUTPUT_FILENAME) as output_f: #TODO открываем полученный JSON-файл на чтение
        for line in output_f: #TODO итерируем по строкам файла
            print(line, end="") #TODO выводим строку без добавления лишнего символа
