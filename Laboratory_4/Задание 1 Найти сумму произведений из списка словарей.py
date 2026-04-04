import json #TODO импорт модуля json для работы с данным форматом

def task() -> float: #TODO задаём функцию, которая вернет число с плавающей точкой
    filename = 'input.json'          #TODO имя файла с данными
    total = 0.0                     #TODO переменная с накопленной суммой произведений

    with open(filename, 'r', encoding='utf-8') as f: #TODO открываем файл на чтение в текстовом режиме с кодировкой UTF-8
        data = json.load(f)  #TODO превращаем JSON в объект Python

    for item in data: #TODO перебираем каждый элемент в списке data
        if 'score' in item and 'weight' in item: #TODO проверяем наличие обоих ключей
            total += item['score'] * item['weight'] #TODO умножаем значения ключей и прибавляем произведение к переменной total

    return round(total, 3) #TODO возвращаем значение, округляем до 3 знаков


print(task()) #TODO вызываем функцию и выводим её результат
