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



from random import randint
from functools import reduce


# Work with imported function of python
def func():

    no_name_func = lambda x: x * randint(1, 10)  # Func that will multiply integer on random integer

    l = []

    for i in range(1, 11):  # Generate the list with integer from 1 to 10
        l.append(i)

    result = list(map((no_name_func), l))  # Used "map" function for multiply integers

    for i in list(filter(lambda x: x % 2, l)):  # The list was filtered and removed odd integers
        l.remove(i)

    s = reduce(lambda x, y: x + y, l)  # At last we gave sum of the items in the list

    print(s)

func()


# Work with personal
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def __str__(self):
        return '[Person has next data: {}, {}, {}]'.format(self.name, self.job, self.pay)

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'Manager', pay)

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)

    def __getattr__(self, item):
        return getattr(self.person, item)

    def __str__(self):
        return str(self.person)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaise(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)






import io


# The class 'Human'
class Human:
    def __init__(self, t):
        self.name = t[0]
        self.last_name = t[1]
        self.age = t[2]
        self.briber = t[3]
        self.brib = None
        self.height = 186
        self.mass = 114

        if self.briber == 'True':
            Deputy.give_tribute(self)

    def __hash__(self):
        return hash(self.name) + hash(self.last_name)

    def __eq__(self, other):
        return self.name == other.name and \
                self.last_name == other.last_name

    def __str__(self):
        return 'Deputy data: {}, {}, {}, {}, {}, {}, {}'.format(self.name, self.last_name, self.age, self.briber, self.brib, self.height, self.mass)


class Deputy(Human):  # This class checks have some deputy criminal money or not
    def give_tribute(self):

        if self.briber == False:
            print('This person is not a briber')
        else:
            brib = int(input('How much money wold like to take this deputy? '))

            if brib > 10000:
                print('This deputy may to go to the police')
            else:
                self.brib = brib


class Fraction:  # Fraction may to create, delete, show deputies, clear fraction and other things
    def add_deputy(self):  # Add deputy and to write him to a file
        print('Input deputy data')

        deputy = input('Name: '), input('Last name: '), input('Age: '), input('Briber: ')

        deputy1 = Deputy(deputy)

        f = open('file.txt', 'a')
        f.write(deputy1.__str__() + '\n')
        f.close()

    def del_deputy(self):  # Delete the deputy from a file, if name and last name the same with deputy data and data that typed the user
        print('Input data of deputy that you want to delete')

        data = input('Name: '), input('Last name: ')  # The user type some data

        with open('file.txt', 'r') as f:  # Open a file with deputies
            lines = f.readlines()

        for line in lines:
            finder = line.find(data[0]), line.find(data[1])  # Check, haves this file deputy or not

            if finder[0] > 1 and finder[1] > 1:  # If program input to the variable index > 0 than deputy is in a file
                lines.remove(line)  # Remofe deputy data from a file

        f.close()

        with open('file.txt', 'w') as f:  # Write deputies to a file
            f.writelines(lines)

        f.close()

    def show_bribers(self):  # Show briber from deputies list

        f = open('file.txt', 'r')

        deputies = [line.split(', ') for line in f.readlines()]  # Add bribers data to the list

        f.close()

        # Add bribers to the list and sort the persons ascending briber
        self.bribers = sorted([deputy for deputy in deputies if deputy[3] == 'True'], key=lambda briber: briber[4], reverse=True)

        return 'All bribers: {} \nSuper briber: {}'.format(self.bribers, self.bribers[0])

    def show_deputies(self):  # Show all deputies

        f = open('file.txt')

        for line in f.readlines():
            print(line)

        f.close()

    def clear_fraction(self):  # Delete all deputies from fraction

        f = open('file.txt', 'w')

        try:
            for line in f.readlines():
                print(line)
        except io.UnsupportedOperation:
            print('Operation is successful, all deputies was deleted')

    def are_deputies(self):  # The fraction haves any deputies or not

        f = open('file.txt')

        if len(f.readlines()) >= 1:
            print('The fraction haves deputies')
        else:
            print('The fraction does not have any deputies')
