# 1.1 Условие
#Напишите программу, которая считывает три числа и выводит их сумму. Каждое число записано в отдельной строке. 

a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

# 1.2 Условие
#Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь. Каждое число записано в отдельной строке. 

b = int(input())
h = int(input())
print(1/2 * b * h)

# 1.3 Условие
#n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику?
#Сколько яблок останется в корзинке? Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа). 

n = int(input())
k = int(input())

print(k // n)
print(k % n)

# 1.4 Условие
# Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные часы в этот момент. Программа должна вывести два числа:
# количество часов (от 0 до 23) и количество минут (от 0 до 59). Учтите, что число n может быть больше, чем количество минут в сутках. 

n = int(input())
print(n // 60 % 24)
print(n % 60)

# 1.5 Условие
# Напишите программу, которая приветствует пользователя, выводя слово Hello, введенное имя и знаки препинания по образцу: 

name = input()
print('Hello, '+name+'!')

# 1.6 Условие
#Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере (пробелы важны!). 

value = int(input())
print('The next number for the number ' + str(value) + ' is ' + str(value + 1) + '.')
print('The previous number for the number ' + str(value) + ' is ' + str(value - 1) + '.')

# 1.7 Условие
#В школе решили набрать три новых математических класса. Так как занятия по математике у них проходят в одно и то же время, было решено выделить кабинет для каждого класса и купить в них новые парты. За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт чтобы их хватило на всех учеников?
#Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов. 

a = int(input())
b = int(input())
c = int(input())

print(str((a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)))

# 1.8 Условие

#Обувная фабрика собирается начать выпуск элитной модели ботинок. Дырочки для шнуровки будут расположены в два ряда, расстояние между рядами равно a
#, а расстояние между дырочками в ряду b. Количество дырочек в каждом ряду равно N. Шнуровка должна происходить элитным способом “наверх, по горизонтали
#в другой ряд, наверх, по горизонтали и т.д.” (см. рисунок). Кроме того, чтобы шнурки можно было завязать элитным бантиком,
#длина свободного конца шнурка должна быть l. Какова должна быть длина шнурка для этих ботинок?

#Программа получает на вход четыре натуральных числа a, b, l и N - именно в таком порядке - и должна вывести одно число - искомую длину шнурка.

a = int(input())
b = int(input())
l = int(input())
N = int(input())

print(a + 2 * (N - 1) * a + 2 * (N - 1) * b + 2 * l)

# 2.1 Условие
#Даны два целых числа. Выведите значение наименьшего из них.  

a = int(input())
b = int(input())

if a > b:
    print(b)
else:
    print(a)

# 2.2 Условие
#В математике функция sign(x) (знак числа) определена так:
#sign(x) = 1, если x > 0,
#sign(x) = -1, если x < 0,
#sign(x) = 0, если x = 0.

#Для данного числа x выведите значение sign(x). Эту задачу желательно решить с использованием каскадных инструкций if... elif... else. 

x = int(input())

if x > 0:
    print('1')
elif x == 0:
    print('0')
else:
    print('-1')
    
# 2.3 Условие
#Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета — то NO.
#Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. 
 
 col_1 = int(input())
row_1 = int(input())
col_2 = int(input())
row_2 = int(input())

if col_1 % 2 == row_1 % 2 and col_2 % 2 == row_2 % 2:
    print('YES')
elif col_1 % 2 != row_1 % 2 and col_2 % 2 != row_2 % 2:
    print('YES')
else:
    print('NO')
    
# 2.4 Условие
#Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является високосным, то выведите YES, иначе выведите NO.
#Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400. 
 
 year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('YES')
else:
    print('NO')
    
# 2.5 Условие
#Даны три целых числа. Выведите значение наименьшего из них. 

a = int(input())
b = int(input())
c = int(input())

if a <= b <= c:
    print(a)
elif b <= a <= c:
    print(b)
else:
    print(c)

# 2.6 Условие
#Даны три целых числа.
#Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны). 
 
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else: 
    print(0)

# 2.7 Условие
#Шахматная ладья ходит по горизонтали или вертикали. Даны две различные клетки шахматной доски, определите, может ли ладья попасть с первой клетки
#на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки,
#потом для второй клетки.
#Программа должна вывести YES, если из первой клетки ходом ладьи можно попасть во вторую или NO в противном случае. 
 
col_1 = int(input())
row_1 = int(input())
col_2 = int(input())
row_2 = int(input())

if (col_1 - col_2) != 0 and (row_2 - row_1) == 0:
    print('YES')
elif (col_1 - col_2) == 0 and (row_2 - row_1) != 0:
    print('YES')
else:
    print('NO')

# 2.8 Условие
#Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку. Даны две различные клетки шахматной доски, определите, может ли король попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки,
#потом для второй клетки. Программа должна вывести YES, если из первой клетки ходом короля можно попасть во вторую или NO в противном случае. 
 
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if ((abs(x1 - x2) == 1) & (y1 == y2)) \
    | ((abs(y1 - y2) == 1) & (x1 == x2)) \
    | ((abs(x1 - x2) == 1) & (abs(y1 - y2) == 1)):
    print('YES')
else: print('NO')

# 2.9 Условие
#Шахматный слон ходит по диагонали. Даны две различные клетки шахматной доски, определите, может ли слон попасть с первой клетки на вторую одним ходом. 
 
 
col_1 = int(input())
row_1 = int(input())
col_2 = int(input())
row_2 = int(input())

if abs(col_2 - col_1) == abs(row_2 - row_1):
    print('YES')
else:
    print('NO')

# 2.10 Условие
#Шахматный ферзь ходит по диагонали,
#горизонтали или вертикали. Даны две различные клетки шахматной доски, определите, может ли ферзь попасть с первой клетки на вторую одним ходом. 
 
col_1 = int(input())
row_1 = int(input())
col_2 = int(input())
row_2 = int(input())

if col_1 == col_2 or row_2 == row_1 or abs(col_2 - col_1) == abs(row_2 - row_1):
    print('YES')
else:
    print('NO')

# 2.11 Условие
#Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали, или наоборот.
#Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую одним ходом.
 
col_1 = int(input())
row_1 = int(input())
col_2 = int(input())
row_2 = int(input())

if abs(col_2 - col_1) == 2 and abs(row_2 - row_1) == 1 or abs(col_2 - col_1) == 1 and abs(row_2 - row_1) == 2:
    print('YES')
else:
    print('NO')

# 2.12 Условие
#Шоколадка имеет вид прямоугольника, разделенного на n×m долек. Шоколадку можно один раз разломить по прямой на две части. Определите, можно ли таким образом
#отломить от шоколадки часть, состоящую ровно из k долек. Программа получает на вход три числа: n, m, k и должна вывести YES или NO. 
 
n = int(input())
m = int(input())
k = int(input())

if n * m >= k and (k % m == 0 or k % n == 0):
    print('YES')
else:
    print('NO')

# 2.13 Условие
#Яша плавал в бассейне размером N × M метров и устал. В этот момент он обнаружил, что находится на расстоянии x метров от одного из длинных бортиков (не обязательно
#от ближайшего) и y метров от одного из коротких бортиков. Какое минимальное расстояние должен проплыть Яша, чтобы выбраться из бассейна на бортик?
#Программа получает на вход числа N, M, x, y. Программа должна вывести число метров, которое нужно проплыть Яше до бортика. 

# Решение втупую:
N = int(input())
M = int(input())
x = int(input())
y = int(input())

if N >= M:
    if x <= M / 2:
        if y <= N / 2:
            if x < y:
                print(x)
            else:
                print(y)
        else:
            if x < (N - y):
                print(x)
            else:
                print(N - y)
    else:
         if y <= N / 2:
            if (M - x) < y:
                print(M - x)
            else:
                print(y)
         else:
            if (M - x) < (N - y):
                print(M - x)
            else:
                print(N - y)
else:
    if x <= N / 2:
        if y <= M / 2:
            if x < y:
                print(x)
            else:
                print(y)
        else:
            if x < (M - y):
                print(x)
            else:
                print(M - y)
    else:
         if y <= M / 2:
            if (N - x) < y:
                print(N - x)
            else:
                print(y)
         else:
            if (N - x) < (M - y):
                print(N - x)
            else:
                print(M - y)
# Решение в умную:
n = int(input())
m = int(input())
x = int(input())
y = int(input())
# n, m = min(n, m), max(n, m)
if n > m:
    n, m = m, n
if x >= n / 2:
    x = n - x
if y >= m / 2:
    y = m - y
# print(min(x, y))
if x < y:
    print(x)
else:
    print(y)

# 3.1 Условие
#Дано натуральное число. Выведите его последнюю цифру. 

num = int(input())
print(num % 10)

# 3.2 Условие
#Длина Московской кольцевой автомобильной дороги —109 километров. Байкер Вася
#стартует с нулевого километра МКАД и едет со скоростью v километров в час. На какой отметке он остановится через t часов?
#Программа получает на вход значение v и t. Если v>0, то Вася движется в положительном направлении по МКАД, если же значение v<0, то в отрицательном.
#Программа должна вывести целое число от 0 до 108 — номер отметки, на которой остановится Вася.

v = int(input())
t = int(input())

if v > 0:
    print(round(v * t % 109))
else:
    print(round((109 + v * t) % 109))

#По-умному:
a = int(input())
b = int(input())
print((a * b) % 109)

# 3.3 Условие
#Дано положительное действительное число X. Выведите его дробную часть. 

X = float(input())
print(X - int(X))

# 3.4 Условие
#Дано положительное действительное число X. Выведите его первую цифру после десятичной точки. 

X = float(input())
print(int((X - int(X)) * 10))

# 3.5 Условие
#В некоторой школе занятия начинаются в 9:00. Продолжительность урока — 45 минут, после 1-го, 3-го, 5-го и т.д. уроков перемена 5 минут, а после 2-го, 4-го,
#6-го и т.д. — 15 минут.
#Дан номер урока (число от 1 до 10). Определите, когда заканчивается указанный урок.
#Выведите два целых числа: время окончания урока в часах и минутах.

from math import floor

n = int(input())

if n % 2 == 1:
    print((n * 45 + floor(n / 2) * (15 + 5)) // 60 + 9)
    print((n * 45 + floor(n / 2) * (15 + 5)) % 60)
else:
    print((n * 45 + floor(n / 2) * 5 + (floor(n / 2) - 1) * 15) // 60 + 9)
    print((n * 45 + floor(n / 2) * 5 + (floor(n / 2) - 1) * 15) % 60)

#По-умному:
a = int(input())
a = a*45 + (a//2)*5 + ((a+1)//2-1)*15
print(a//60 + 9, a%60)

# 3.6 Условие
#За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? Программа получает на вход числа n и m. 

n = int(input())
m = int(input())

if m // n * n == m:
    print(m // n)
else:
    print(m // n + 1)
# 3.7 Условие
#Пирожок в столовой стоит a рублей и b копеек. Определите, сколько рублей и копеек нужно заплатить за n пирожков.
#Программа получает на вход три числа: a, b, n, и должна вывести два числа: стоимость покупки в рублях и копейках. 

a = int(input())
b = int(input())
n = int(input())

print(a * n + b * n // 100)
print(b * n % 100)

# 3.8 Условие
#Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы, минуты и секунды для каждого из моментов времени. Известно, что второй момент
#времени наступил не раньше первого. Определите, сколько секунд прошло между двумя моментами времени.
#Программа на вход получает три целых числа: часы, минуты, секунды, задающие первый момент времени и три целых числа, задающих второй момент времени.
#Выведите число секунд между этими моментами времени.

h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
print((h2 - h1) * 3600 + (m2 - m1) * 60 + s2 - s1)

# 3.9 Условие
#Улитка ползет по вертикальному шесту высотой h метров, поднимаясь за день на a метров, а за ночь спускаясь на b метров.
#На какой день улитка доползет до вершины шеста? Программа получает на вход натуральные числа h, a, b.
#Программа должна вывести одно натуральное число. Гарантируется, что a>b.

from math import ceil

h = int(input())
a = int(input())
b = int(input())

print(ceil((h - a) / (a - b)) + 1)

# 3.10 Условие
#Дано натуральное число. Найдите число десятков в его десятичной записи. 

a = int(input())
print((a % 100 - a % 10) / 10)

# 3.11 Условие
#Дано трехзначное число. Найдите сумму его цифр.

a = int(input())

print(a // 100 + a // 10 % 10 + a % 10)

# 3.12 Условие
# Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами. 

from math import sqrt

a = int(input())
b = int(input())

print(sqrt(a ** 2 + b ** 2))

# 3.13 Условие
#С начала суток прошло H часов, M минут, S секунд (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). По данным числам H, M, S определите угол (в градусах),
#на который повернулаcь часовая стрелка с начала суток и выведите его в виде действительного числа. 

H = int(input())
M = int(input())
S = int(input())

print(30 * H + 0.5 * M + 0.5 / 60 * S)

# 3.14 Условие
#С начала суток часовая стрелка повернулась на угол в α градусов. Определите на какой угол повернулась
#минутная стрелка с начала последнего часа. Входные и выходные данные — действительные числа. 

alpha = float(input())

print(alpha % 30 / 30 * 360)

# 3.15 Условие
#С начала суток часовая стрелка повернулась на угол в α градусов. Определите сколько полных часов, минут и секунд прошло с начала суток, то есть решите задачу,
#обратную задаче «Часы - 1». Запишите ответ в три переменные и выведите их на экран. 

alpha = float(input())

print(alpha // 30, alpha % 30 // 0.5, int((alpha % 30 % 0.5) * 120) )

# 3.16 Условие
#Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада. Вклад составляет X рублей Y копеек. Определите размер вклада
#через год.
#Программа получает на вход целые числа P, X, Y и должна вывести два числа: величину вклада через год в рублях и копейках. Дробная часть копеек отбрасывается. 

P = int(input())
X = int(input())
Y = int(input())

sum = X * 100 + Y
perc = P / 100
print(X + (Y + sum * perc) // 100, int((Y + sum * perc) % 100))
