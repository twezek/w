# імпортіруєм бібліотеку
from colorama import init
from colorama import Fore, Back, Style
init()
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# робить українську мову 

from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ua'

# код для роботи

owm = OWM('f3895945b5ce7406694ff2424bc4d159')
mgr = owm.weather_manager()

# зберігаємо все в dict щоб вивести всю інформацію за погоду

wlist = []

# робим цикл

print( Fore.BLACK)
while True:
    #запитуєм користувчача
    print(Back.GREEN)
    place = input('Де ви хочете дізнатись погоду? : ')  

     #обробля помилки    

    try:
        observation = mgr.weather_at_place(place)
        weather = observation.weather
    except:
        print(" Не вдалося знайти це місце. Спробуйте ще раз.")
        continue

    # описуєм команди для погоди
    print(Back.BLUE)
    observation = mgr.weather_at_place(place) 
    weather = observation.weather  
    temp = weather.temperature('celsius')['temp']     # температура
    status = weather.detailed_status          # опис (наприклад, "хмарно")
    speed = weather.wind()                    # швидкість та напрямок вітру
    water = weather.humidity                  # вологість

    # добавляєм в дікт все шоб зберегти і знову потім вивести 
    wlist.append({
    "місто": place,
    "температура": temp,
    "опис": status,
    "вітер": speed,
    "вологість": water
    })

    #виводим результат

    print(f'Зараз у місті {place}: {status}')     
    print(f'Температура: {temp}')
    print(f"Швидкість вітру: {speed}")
    print(f'Вологість: {water}')

    #запитуєм чи не хоче ще дізнатись інформацію десь
    
    print(Back.RED)
    print('Хочеш дізнатись інформацію ще десь? Чи показати історію пошуку? ')
    print('Так/Ні/історію ')
    user1 = input().lower()     

    if user1 == 'ні':
        print('Добре.')
        break
    elif user1 == 'історію':
        for record in wlist:
            print(f"\nМісто: {record['місто']}")
            print(f"Температура: {record['температура']}")
            print(f"Погода: {record['опис']}")
            print(f"Вітер: {record['вітер']}")
            print(f"Вологість: {record['вологість']}")
        break
    else:
        print('Добре давай спробуємо ще раз! ')

user2 = input("Натисніть щоб закрити: ")