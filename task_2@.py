
import random

def get_numbers_ticket(min, max, quantity):
    save = []#Порожній список для рандомних чисел
    result = []#Порожній список для результану чисел
    
    while quantity > 0:#Цикл з рандомом для створення списку 
        save.append(random.randrange(min, max, 1))#Записуємо по числу в список за цикл
        quantity = quantity - 1   #Віднімаємо від заданого числа по одному за цикл
    
    for i in save:#Цикл для відбору одникових значень в списку "save"
        if i not in result:#Порівнюю списки
            result.append(i)#Добавляю в список значення
        else: result.append(random.randint(min, max))#Якщо число повторюється то замінюю його рондомним
    
    result.sort()#Сортую список
    return result#Повертаю результат


lottery_numbers = get_numbers_ticket(1, 36, 5)#Зберігаю результат функції
print("Ваші лотерейні числа:", lottery_numbers)#Виводжу збережений результат



