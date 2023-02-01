import data
def import_data():
    print('Импортирует данные: ')
    f = open("import1_data.txt")
    print("file.mode: " + f.mode)
    print("file.name: " + f.name)
    for line in f:
        print(line)
        table_1 = []
        table_1.append(line.strip('\n'))
        data.phone_help.append(table_1)
    f.close()
    print('КОНЕЦ ИМПОРТА: ')
