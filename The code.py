'''
#Ex 1
a = input()
b = a[::-1]#Розворот строки
print(b)
'''



#Ex1.2
a = str(input())
a = a.split(' ')#Розбиваємо слова за допомогою методу:
print(len(a))#Підраховуємо кількість розбитих елементів





#Exersis 2
#Додаємо до словника ще 2 ключ-значення
rivers = {'Amazon': 'America',
}
rivers['Nil'] = 'Africa'
rivers['Dnipro'] = 'Ukraina'     
print(rivers)

#Використовуємо %s-знак для того, щоб замінити його на ключ-значення-.items()
#зі словника
for river, region in rivers.items():
    print('The river %s are in %s region!' % (river, region))



#Exersis 3
#Якщо х замінити на одне зі слів які прирівнюються до х тоді в нас буде виведено відповідне йому значення
e2g = {'stork': 'storch', 'hawk':'woodpecker', 'owl':'eule'}
def word(x):
    if x == 'stork':
        print('storch')
    elif x == 'hawk':
        print('woodpecker')
    elif x == 'owl':
        print('eule')
    else:
        print('Pleas, input a corect word')
word('owl')
#додаємо ключ-значення до словника іншим способом
other = {'book': 'buch', 'car': 'auto'}
e2g.update(other)
print(e2g)

#Виводимо словник, ключ і значення в вигляді списку
for key, values in e2g.items():
    print(key, values)

for key, values in e2g.items():
    print(values)

for key, vakues in e2g.items():
    print(key)






#Exersis 4
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print(inventory)


#will sorted the key 'backpack' and print his
inventory['backpack'].sort()
print(inventory)


#Видаляємо bagger
inventory['backpack'].remove('bagger')
print(inventory)


#Додаємо 50 до значення ключа gold
inventory['gold'] +=50
print(inventory['gold'])


#Ex 5
#Створюємо словник
prices = {}
other = {"banana": 4,
         "apple": 2,
         "orange": 1.5,
         "pear": 3
}

#Вставляємо словник other in prices
prices.update(other)
print(prices)

#Створюємо словник stock
stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
   "pear": 15
}


#Використовуємо наступну операцію для послідовного отримання результатів
#Для кожного ключа в словнику prices, видрукуй кожен ключ.
for x in prices:
    print(x)
#Видрукуй значення ключів зі словника prices/Додаємо деякий текс для кращого вигляду
    print('Ціна %s' % prices[x])
#Видрукуй значення ключів зі словника stock
    print('Залишок %s' % stock[x])

#Перемножуємо значення
total = 0
for x in prices:
    (prices[x] * stock[x])
#Отримуємо їх суму
    total = total + prices[x] * stock[x]
print (total)




#Ex6
#Створюємо словники
lloyd = { "name": "Lloyd", "homework": [90.0,97.0,75.0,92.0],  "quizzes": [88.0,40.0,94.0], "tests": [75.0,90.0] }
alice = {"name": "Alice", "homework": [100.0, 92.0, 98.0, 100.0],  "quizzes": [82.0, 83.0, 91.0], "tests": [89.0, 97.0] }
tyler = { "name": "Tyler",  "homework": [0.0, 87.0, 75.0, 22.0], "quizzes": [0.0, 75.0, 78.0],  "tests": [100.0, 100.0] }

#Об'єднуємо словники в список для зручнішої роботи з данними
students = [lloyd, alice, tyler]

#Виводимо данні зі словника через цикл за допомогою списку
for student in students:
    print (student['name'])
    print (student['homework'])
    print (student['quizzes'])
    print (student['tests'])

#Сумуємо числа і виводимо їх середнє значення
def avarage(x):
    total = sum(x)#Виводить суму чисел
    total = float(total)#Конвертує в числа з плаваючою точкою
    return total / len(x)#Виводимо середнє значення за допомогою ділення суми на кількість

#Створюємо функцію яка буде виводити бали студента
def get_letter_grade(s):
    if s >= 90:
        print ('Your level A')
    elif s <= 90 and s >= 70: #Якщо бал(s)-цифра буде менша 90 and-і більшф 70 тоді виводь на екран:
        print ('Your level B')
    elif s <= 70 and s >= 50:
        print ('Your level C')
    else:
        print('You must to try one more time')
get_letter_grade(49)#Задаємо бали і отримуємо результат  

# Завдання-1 Напишіть функцію яка виводить максимальне число
def max_of_three(*args):
    a = list(args)
    a.sort()
    return a[-1]
print(max_of_three(10, 4, 5))

#Завдання-2 Написати функцію яка виводить найдовше слово
def random_from_list(*args):
    lst = list(args)
    for x in lst:
        if len(x) > 0:
            return x
print(random_from_list(max(['Name','My name', 'Your name'])))

#Завдання-3
import random
def summarizer():
    result = 0
    #def random_10():
    while result < 100:
        a = random.randint(1, 10)
        result += a
        if result >= 100:
            return result
            break
print(summarizer())


    
#функція для підрахунку значень іменнованих aргументів
def func(**args):
    res = []
    for v in args.values():
        res.append(v)
    return sum(res)

def adder(**args):
    res = list(args.values())
    first = res[0]
    for other in res[1:]:
        first += other
    return first

print(func(a = 6, b = 9))
print(adder(a = 3, b = 4))

    


#Якщо числа однакові, поверни їх суму помножену на їх кількість, інакше поверни їх суму
def num(a, b, c)
    if a == b and b == c:
        d = a + b + c
        return d * 3
    else:
        return a + b + c

#Додай на початок строки "Is " якщо вона так не починається
def string(a):
    if a.lower().startswith('is'):
        return a
    else:
        a = a.lower()
        return 'Is ' + a
        
#Easy "Random Game with two Units"
import random


class Warrior:
    attack = 20


unit = Warrior()

enemy = Warrior()

unit.health = 100
enemy.health = 100


def func(a, b):
    while a.health >= 1 and b.health >= 1:
        i = random.randint(-1, 1)
        if i == -1:
            a.health -= b.attack
            print('d do attack on a', '/a have: ', a.health, 'health')
        elif i == 1:
            b.health -= a.attack
            print('a do attack on b', '/b have: ', b.health, 'health')
        else:
            a.health += 20
            b.health += 20
            print('Regeneration')


func(unit, enemy)


#Work with personal of some commpany
class Person:
    def __init__(self, name, surname, qualification=1):
        self.name = name
        self.surname = surname
        self.qualification = qualification

    def worker_info(self):
        print('Worker has next data: ', self.name, self.surname, ' has qualification: ', self.qualification)

    def __del__(self):
        print('До свидания, мистер: ', self.name)


worker3 = Person('Dimitry', 'Paliniuk', qualification=5)
worker1 = Person('Anastasia', 'Perdoliuk', qualification=7)
worker2 = Person('Wladimir', 'Hardalenko',  qualification=6)


def func(a, b, c):
    l = [a, b, c]
    fate = []
    for i in l:
        i.worker_info()
        fate.append(i.qualification)
    fate.sort()
    for i in l:
        if i.qualification == fate[0]:
            i.__del__()


func(worker3, worker2, worker1)
input()



#Managment of students in some class
lloyd = { "name": "Lloyd", "homework": [90.0,97.0,75.0,92.0],  "quizzes": [88.0,40.0,94.0], "tests": [75.0,90.0] }
alice = {"name": "Alice", "homework": [100.0, 92.0, 98.0, 100.0],  "quizzes": [82.0, 83.0, 91.0], "tests": [89.0, 97.0] }
tyler = { "name": "Tyler",  "homework": [0.0, 87.0, 75.0, 22.0], "quizzes": [0.0, 75.0, 78.0],  "tests": [100.0, 100.0] }

students = [lloyd, alice, tyler]

index = 0

while index < 3:
    for key, value in students[index].items():
        print(key, value,)

    index += 1
    print('\n')


def func(*args):
    index = 0

    Lloyd = 0
    Alice = 0
    Tyler = 0

    while index < 3:
        homework_l = students[index]['homework']
        quizzes_l = students[index]['quizzes']
        tests_l = students[index]['tests']

        mid_h = float('{0:.1f}'.format(sum(homework_l) / len(homework_l)))
        mid_q = float('{0:.1f}'.format(sum(quizzes_l) / len(quizzes_l)))
        mid_t = float('{0:.1f}'.format(sum(tests_l) / len(tests_l)))

        total = float('{0:.1f}'.format((mid_h + mid_q + mid_t) / 3))

        print(students[index]['name'], mid_h, mid_q, mid_t, total)

        students[index]['mark'] = total

        if index == 0:
            Lloyd += total
            print(Lloyd)
        elif index == 1:
            Alice += total
            print(Alice)
        else:
            Tyler += total
            print(Tyler)

        index += 1
    return Lloyd, Alice, Tyler


func(students)


def mark(*args):
    index = 0

    while index < 3:
        if students[index]['mark'] > 90:
            print(students[index]['name'], 'has: A')

        elif students[index]['mark'] < 90 and students[index]['mark'] > 70:
            print(students[index]['name'], 'has: B')

        elif students[index]['mark'] < 70 and students[index]['mark'] > 50:
            print(students[index]['name'], 'has: C')

        else:
            print(students[index]['name'], 'has: D')

        index += 1

    middle_mark = (float(students[0]['mark'] + students[1]['mark'] + students[2]['mark'])) / 3

    print('\----------------------------------------------/')

    print('middle mark of this class: {0:.1f}'.format(middle_mark))

    if middle_mark > 90:
        print('middle mark of this class: A')

    elif middle_mark > 70 and middle_mark < 90:
        print('middle mark of this class: B')

    elif middle_mark > 50 and middle_mark < 70:
        print('middle mark of this class: C')

    else:
        print('middle mark of this class: D')


mark(students)


#how to change size of the item in some string

def func():
    s = 'string'
    l = []
    ind = 0

    for i in s:
        if i == s[ind]:
            s = s.replace(i, s[ind].upper())
            l.append(s)
            ind += 1
            
    ind = 0
    for i in s:
        if i == s[ind]:
            s = s.replace(i, s[ind].lower())
            l.append(s)
            ind += 1
    print(l)
func()




numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
ukr = 'а, б, в, г, ґ, д, е, є, ж, з, и, і, ї, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ь, ю, я'.replace(', ', '')

password = input('Input your password: ')






# Work with passwords
def func(password):
    if len(password) < 6:  # Check weight of the password
        print('Your password is too short')
    else:

        def check(password, arg):  # Create function that to check, have the password all the important figures or not
            for i in arg:
                ind = password.find(i)
                # print(ind)

                if ind > -1:  # if yes then return True
                    return True

        for i in ukr:  # The password has any item from ukr literal
            ind = password.find(i)

            if ind > -1:  # If yes, show next message
                print('Your password mast have next items: {}, {}, {}, {}'.format(numbers, lower_case, upper_case, special_characters))
                break
            else:
                # Call 'check' function
                num_res = check(password, numbers)
                low_res = check(password, lower_case)
                upe_res = check(password, upper_case)
                spe_res = check(password, special_characters)

                if num_res == True and low_res == True and upe_res == True and spe_res == True:  # If all the called functions return True
                    print('Your password is correct')
                else:
                    print('Your password mast have next items: {}, {}, {}, {}'.format(numbers, lower_case, upper_case, special_characters))
            break


func(password)



from random import randint


# The decorator which calls "gen_random" func 20 times
def retry(func):
    def wrapper():
        n = 0
        while n < 20:

            if func() == 1:  # If result of "gen_random" is 1
                print('success')
                break

            n += 1
            if n == 20:  # If "gen_random" doesn't return 1 after called 20 times
                print('no')
    return wrapper()


# Func which generates random numbers
@retry
def gen_random():
    r = randint(1, 10)

    if r == 1:
        return r
    else:
        return ImportError


# Func which calls "gen_random"
def run():
    result = gen_random()
    return result


