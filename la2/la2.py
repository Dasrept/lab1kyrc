def describe_person(name, age=30):
    return f'Имя: {name}, Возраст: {age}'

def inf():
    while True:
        name = input('Введите имя (Или "стоп" для выхода): ')
        if name.lower() == 'стоп':
            print('Программа завершена :)')
            return

        age_input = input('Введите возраст: ')
        if age_input.lower() == 'стоп':
            print('Программа завершена')
            return

        if age_input == '':
            print(describe_person(name))
        else:
            try:
                age = int(age_input)
                print(describe_person(name, age))
            except ValueError:
                print('Введите число, а не слово!')
                continue
print(inf())