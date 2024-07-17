

#Щоб перевірити, що рядок починається з підрядка, є метод startswith:

#список номерів
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

normal = []
nor =""

def normalize_phone(phone_number) -> list:
    # for num in phone_number:
    number = phone_number.strip(r" \d\\t+")
            
    print(number)
 
    # return number


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)










# from datetime import datetime, timedelta


# def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    
#     today = datetime.today().date() #Змінна з поточною датою
#     results = [] #Змінна для результату
    
#     for user in users: #Цикл для читання списку
        
#         birthday = datetime.strptime(user["birthday"], '%Y.%m.%d').date() #Стріпаємо день народження в об'єкт datetime
        
#         birt_this_year = birthday.replace(year=today.year) #Витягуємо рік з дати народження
        
#         congr_date = user["birthday"] #Змінна для дати привітання
        
#         dayOfWeek = birt_this_year.weekday() #Записуємо день тижня
        
#         res_bird = int((birt_this_year - today).days) #Віднімаємо теперішню дату від дня нородження
        
#         nam = user["name"] #Змінна для name
        
        
#         s = {}
#         s.update({"name": nam})
        
        
#         if res_bird <= 7 and res_bird >= 0:      
#             if dayOfWeek > 4:
#                 days_to_monday = 7 - dayOfWeek
#                 birthday = birthday + timedelta(days=days_to_monday)  
#             birthday = str(birthday)
#             results.append(s)
        
#         s.update({"congratulation_date": birthday})          
        

#     return results

# users = [
#     {"name": "Jane Smith", "birthday": "1990.07.17"},
#     {"name": "Dima Ilin", "birthday": "1997.07.21"},
#     {"name": "John Doe", "birthday": "1968.07.20"},
#     {"name": "Bred Lohan", "birthday": "1985.01.23"},
#     {"name": "Viktoria Lopes", "birthday": "2001.07.11"}
# ]

# upcoming_birthdays = get_upcoming_birthdays(users)
# print("Список привітань на цьому тижні:", upcoming_birthdays)





# # my_list = [1, "Hello", 3.14]
# # my_list.append(4)
# # print(my_list)

# from datetime import datetime



# greeting = "Happy Birthday"
# score_bird = "Days until the birthday"

# def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
#     today = datetime.today().date()
    
    
#     for user in users:
#         birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
#         birt_this_year = birthday.replace(year=today.year)
#         res_bird = int((birt_this_year - today).days)
        
#         # print((today - birt_this_year).days)
#         if today >= birt_this_year:
#             print("In the next year")    
#         if today == birt_this_year:
#             print(greeting)
#         if res_bird <= 7:
#             print("222")
        
#         # print(greeting)
#         print(res_bird)
#         # print(birt_this_year)
        
#         # if birt_this_year < today:
#         #     print(f"@@@{(today - birt_this_year).days}")
#         # if birt_this_year == today:
#         #     print("Happy Birthday!!!!")
#         # if birt_this_year < 7:
#         #     print("()()()()")


#         # if birt_this_year == today:
#         #     birth_rs.append(f"Happy Birthday-{name_user}")
#         # if birt_this_year == today:
#         #     res = (f"Happy Birthday!!! '{name_user}'")
#         #     results.append(res)
            
#         print("-----------------")
    
    
    
                
    
#     # print(birthday)
    
#     return f"{users}"


# users = [
#     {"name": "John Doe", "birthday": "1968.07.10"},
#     {"name": "Dima Ilin", "birthday": "1997.06.14"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Viktoria Lopes", "birthday": "2001.07.11"},
#     {"name": "Jane Smith", "birthday": "1990.07.12"}
# ]

# upcoming_birthdays = get_upcoming_birthdays(users)
# print("Список привітань на цьому тижні:", upcoming_birthdays)






# import random


# def get_numbers_ticket(min, max, quantity):
#     save = []
#     res = []
    
#     def randon_range(min, max):  
#         nonlocal save
#         save = random.randrange(min, max, 1)
        
    
#     randon_range(min, max)
#     res.append(save)
#     quantity = quantity - 1 
    
    
        
#     print(save)
#     return res


# lottery_numbers = get_numbers_ticket(1, 36, 5)
# print("Ваші лотерейні числа:", lottery_numbers)




# ##_________________________________________###
# def clean_list(list_to_clean):
#     a=list_to_clean
#     b=[]
#     for i in a:
#         if i not in b:
#             b.append(i)
#         # else: b.append(0)
#     print(b)       
    
#     return b
# print(clean_list([1,1,2,3,3]))
# ##_________________________________________###
