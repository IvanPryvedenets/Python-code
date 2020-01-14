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




