"""
    1. именуй файлы нормально (меньше пробелов и верхнего регистра)
    2. кто тебя надоумил ставить пробел перед скобкой? (print ())
    3. зачем ты импортируешь весь модуль? from datetime import * импортируй
       только ту единственную функциою которую используешь
    4. меньше лишних ненужных пустых строк, кодстиль смотреть в
       PEP0008 (http://pep8.ru/doc/pep8/ - Пустые строки)
    5. зачем ты обернул вывод datetime.strftime в tuple?
"""

from datetime import datetime

print('Начало диапазона: ')
t = True
while t:
    try:
        user_one = int(input(': '))
    except:
        print("Только числа")
        continue
    break

print('Конец диапазона: ')
p = True
while p:
    try:
        user_two = int(input(': '))
    except:
        print("Только числа")
        continue

    if user_two < user_one:
        print('Второе больше первого!')
        continue
    else:
        break

time = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
log = open('loge ' + time + '.txt', 'w')
for i in range(user_one,user_two + 1):
    if i % 2 == 0:
        log.write(str(i) + '   :четное \n')
    else:
        log.write(str(i) + '   :нечетное \n')
print('Файл добавлен')
