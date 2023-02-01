import data
def interdata():
    print('Ввожу данные вручную ')

    second_name = input('Введите Фамилию человека: ')
    first_name = input('Введите Имя человека: ')
    phone_human = input('Введите Телефон человека: ')

    table_1 = []
    table_1.append(second_name)
    table_1.append(first_name)
    table_1.append(phone_human)
    data.phone_help.append(table_1)
    print('Запись добавлена!')
