import data
def export_2_data():
    print('Экспортирует данные 2')

    my_file = open("Export2_File.txt", "w+")
    for record in data.phone_help:
        my_file.write(str(record).strip('[]'))
        my_file.write('\n')
    my_file.close()
    print('Конец экспорта данных ')