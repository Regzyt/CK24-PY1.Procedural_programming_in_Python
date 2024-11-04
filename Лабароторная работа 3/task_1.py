# TODO Напишите функцию для поиска индекса товара
def finder(spisok_list, tovar):
    s = 0
    for i in range(len(spisok_list)):
        if tovar in spisok_list:
            if i == spisok_list.index(tovar) and s == 0:
                s += 1
                return i
        else:
            return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = finder(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
