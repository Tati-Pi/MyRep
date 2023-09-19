#========1==========
user_name = input('Введите ваше имя: ')
user_surname = input('Введите вашу фамилию: ')
user_year_of_birth = int(input('Ведите ваш год рождения: '))
user_age = 2023 - user_year_of_birth
print(user_name,user_surname,',', user_age )

#========2========
number = input("Введите число: ")
number_ = int(number)
number1 = number_ + 1
number2 = number_ - 1
print(f"Следующее за числом {number} число: {number1}\nДля числа {number} предыдущее число: {number2}" )

#========3========
minutes = int(input())
hour = minutes//60
remainder = minutes%60
print(f"{minutes} мин - это {hour} час {remainder} мин" )

#========4========
n = int(input())
n1 = str(n)
print(f'сумма цифр: {int(n1[0])+int(n1[1])+int(n1[2])}\nпроизведение цифр: {int(n1[0])*int(n1[1])*int(n1[2])}')

#========5========
mil1 = input()
mil2 = input()
mili = mil1 + '.' + mil2
mili = float(mili)
calculator = round(mili * 1.61, 1)
print(f'{mili} мили = {calculator} км')
