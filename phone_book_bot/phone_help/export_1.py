import data
def export_1_data():
    print('Экспортирует данные 1')

    my_file = open("Export1_File.txt", "w+")
    for record in data.phone_help:
        my_file.write(str(record).strip('[]'))
    my_file.close()
    print('Конец экспорта данных ')