# Задача 1. В каждой группе учится от 20 до 30 студентов. 
# По итогам экзамена все оценки заносятся в таблицу. 
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

import random

rows = 7
columns = random.randint(20,30)
numbers = [0] * rows
count = 0
scores = 0
beautyText = 1
theBestGroupScores = 0
theBestGroupNumber = 0

for i in range(len(numbers)):
    columns =  random.randint(20,30)
    numbers[i] = list(0 for _ in range(columns))
    for j in range(columns):
        numbers[i][j] = random.randint(2,5)
        count += numbers[i][j]
    scores = count / columns

    if theBestGroupScores < scores:
        theBestGroupScores = scores
        theBestGroupNumber = beautyText
    print(f'Средний балл группы {beautyText}:')    
    print(scores)
    count = 0
    beautyText += 1

print('\nОбщая таблица групп:')
for row in numbers:
    print(row)

print(f'\nЛучшая группа № {theBestGroupNumber} со средним баллом {theBestGroupScores}')
