from funcs import add, subtract

if __name__ == '__main__':
    first_number = int(input('Введите первое число '))
    second_number = int(input('Введите второе число '))
    print(add(first_number, second_number))
    print(subtract(first_number, second_number))
