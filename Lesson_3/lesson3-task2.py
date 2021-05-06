name = input('Введите имя')
surname = input('Введите фамилию')
year = int(input('Введите ваш год рождения'))
city = input('Введите ваш город')
email = input('Введите ваш email')
telephone = input('Введите ваш телефон')


def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname, name, year, city, email,
              telephone))
