 
from datetime import datetime

date_str = input("Введіть дату: ") #Записую в змінну в ведену дату


def get_days_from_today(date_str): #Функція обрахунку
    date_s = 0 #Сюди зберігаю вхідний список 
    
    date_s = date_str.split("-")#Робимо список вхідної дати і обрізаємо "-"
    
    try: #Роблю перевірку на правильний формат одразу після split і пробую прогнати по коду..
        
        date_parameters = datetime(year=int(date_s[0]), month=int(date_s[1]), day=int(date_s[2])).date()  #Створюємо змінну з параметрами вхідного списку
        now_date = datetime.today().date() #Створюємо змінну з поточною датою 
        date_r = now_date - date_parameters # Шукаємо різницю
        return date_r.days #Вертаю число днів
    
    except: #Виводжу попередження про неправильний формат
        return f"Невірний формат дати \n'Введіть в форматі: (yyyy-mm-dd)->2021-12-09'"
        # print("Невірний формат дати")
        # print("Введіть в форматі: (yyyy-mm-dd)->2021-12-09")


#Виводжу результат
res = get_days_from_today(date_str)
print(res)