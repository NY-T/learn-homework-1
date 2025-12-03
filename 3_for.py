"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dictionary_phone = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
    count = 0
    sum_item = 0
    list_items = []
    for i in dictionary_phone:
        print(f'Общее количество проданных {i['product']} - {sum(i['items_sold'])}')
    print()
    for i in dictionary_phone:
        print(f'Среднее количество продаж {i['product']} - {round(sum(i['items_sold'])/len(i['items_sold']), 2)}')
    print()
    for i in dictionary_phone:
        count += sum(i['items_sold'])
    print(f'Суммарное количество продаж всех товаров - {count}')
    print()
    for i in dictionary_phone:
        for x in i['items_sold']:
            list_items.append(x)
        sum_item += sum(i['items_sold'])
    print(f'Среднее количество продаж всех товаров - {round(sum_item / len(list_items), 2)}')
    
if __name__ == "__main__":
    main()
