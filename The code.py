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



# Модуль, який вираховує час виконання функції
import time, sys
trace = lambda *args: None # or print
timefunc = time.clock if sys.platform == 'win32' else time.time


def timer(func, *pargs, _reps = 1000, **kargs):
    trace(func, pargs, kargs, _reps)
    start = timefunc()
    for i in range(_reps):
        ret = func(*pargs, **kargs)
    elapsed = timefunc() - start
    return (elapsed, ret)

def best(func, *pargs, _reps=50, **kargs):
    best = 2 ** 32
    for i in range(_reps):
        (time, ret) = timer(func, *pargs, _reps=1, **kargs)
        if time < best: best = time
    return (best, ret)


# Результати та порівння тривалості виконання різних типів функцій
import sys, mytime

reps = 10000
repslist = range(reps)


def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res

def listComp():
    return[abs(x) for x in repslist]


def mapCall():
    return list(map(abs, repslist))

def genExpr():
    return list(abs(x) for x in repslist)

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())


print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    elapsed, result = mytime.timer(test)
    print('-' * 33)
    print('%-9s: %.5f => [%s...%s]' %
          (test.__name__,elapsed, result[0], result[-1]))

    
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

    

#Вдосконалений варіант функції, яка вираховує час виконання коду
import time, sys
reps = 1000
repslist = range(reps)


def timer(func, *pargs, **kargs):
    start = time.clock()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = time.clock() - start
    return (elapsed, ret)


def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res

def listComp():
    return [abs(x) for x in repslist]

def mapCall():
    return list(map(abs, repslist))

def genExpr():
    return list(abs(x) for x in repslist)

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())

print(sys.version)


for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    elapsed, result = timer(test)
    print('-' * 33)
    print('%-9s: %.5f => [%s...%s]' %
 (test.__name__, elapsed, result[0], result[-1]))





    


