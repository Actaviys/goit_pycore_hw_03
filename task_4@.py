

from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    
    today = datetime.today().date() #Змінна з поточною датою
    results = [] #Змінна для результату
    
    for user in users: #Цикл для читання списку
        
        birthday = datetime.strptime(user["birthday"], '%Y.%m.%d').date() #Стріпаємо день народження в об'єкт datetime
        
        birt_this_year = birthday.replace(year=today.year) #Витягуємо рік з дати народження
        
        dayOfWeek = birt_this_year.weekday() #Записуємо день тижня
        
        res_bird = int((birt_this_year - today).days) #Віднімаємо теперішню дату від дня нородження
        
        nam = user["name"] #Змінна для name
        
        
        s = {} #Змінна для словника
        s.update({"name": nam}) #Добавляємо ім'я до словника
        
        
        if res_bird <= 7 and res_bird >= 0: #Перевіряємо чи на цьому тижні 'ДН - день народження'
            if dayOfWeek > 4: #Перевіряємо чи попадає ДН на вихідні
                days_to_monday = 7 - dayOfWeek #Шукаємо різницю між днем тижня
                birthday = birthday + timedelta(days=days_to_monday) #Додаємо різницю до ДН
            birthday = str(birthday) #Конвертую ДН в string для запису в словник
            results.append(s) #Добавляю перевірені ДН до результату
        
        s.update({"congratulation_date": birthday}) #Добавляємо відкорегований день народження до словника 
        

    return results #Повертаю результат

users = [
    {"name": "Jane Smith", "birthday": "1990.07.17"},
    {"name": "Dima Ilin", "birthday": "1997.07.21"},
    {"name": "John Doe", "birthday": "1968.07.20"},
    {"name": "Bred Lohan", "birthday": "1985.01.23"},
    {"name": "Viktoria Lopes", "birthday": "2001.07.11"}
]

#Виводжу результат
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

