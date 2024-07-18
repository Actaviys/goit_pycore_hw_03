
import re

#список номерів
raw_numbers = [
    "8067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


def normalize_phone(phone_number) -> list:
    phone_number = re.findall(r"[+0123456789]", phone_number)#Витягую в список всі цифри з +
    number = str(''.join(phone_number))#Об'єдную список і перетворюю в рядок
    num_len = len(number)#Рахую кількість символів
    
    #Добавляю потрібні символи в залежності від довжини номера
    if num_len == 12:
        number = f"+{number}"#Форматую рядок з потрібним номером
        
    if num_len == 11:
        number = f"+3{number}"#Форматую рядок з потрібним номером
        
    if num_len == 10:
        number = f"+38{number}"#Форматую рядок з потрібним номером
    
    return number #Повертаю номер


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
