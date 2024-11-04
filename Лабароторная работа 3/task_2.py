# TODO Напишите функцию find_common_participants
def find_common_participants(stroka_one, stroka_two, a=','):
    stroka1 = stroka_one.split(a)
    stroka2 = stroka_two.split(a)
    stroka_all = []
    if len(stroka1) >= len(stroka2):
        for i in stroka1:
            if i in stroka2:
                stroka_all.append(i)
        return stroka_all
    elif len(stroka1) <= len(stroka2):
        for i in stroka2:
            if i in stroka1:
                stroka_all.append(i)
        return stroka_all

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))