# age = input ("Ile masz lat: ")
# months = int(age) * 12
# print("Zyjesz na swiecie", months, "miesiecy!")
#
# EARTH_PERIMETER = 40075
# distance = input("Ile kilometrow przeszedles w tym tygodniu: ")
# weeks = EARTH_PERIMETER / int(distance)
# print("Obejscie Ziemi zajmie Tobie", weeks, "tygodni!")
#
# start_value = input("Podaj poczatkowa wartosc lokaty (zl): ")
# percent = input("Podaj oprocentowanie lokaty (%): ")
# duration = input("Poda czas trwania (lata): ")
#
# value = float(start_value) * (1 + float(percent) / 100) ** int(duration)
# print(f"Wartosc lokaty po {duration} bedzie wynosila: {value} zl")
# print(int(7.8))

# apple_price_biedronka = float(input("Podaj cene jablek w Biedronce: "))
# apple_price_lidl = float(input("Podaj cene jablek w Lidlu: "))
# apple_price_zabka = float(input("Podaj cene jablek w Zabce: "))
#
# min_price = min(apple_price_biedronka, apple_price_lidl, apple_price_zabka)
# max_price = max(apple_price_biedronka, apple_price_lidl, apple_price_zabka)
# print(f"Cena najtanszych jablek to: {min_price} zl")
# print(f"Cena najdrozszych jablek to: {max_price} zl")

# distance = 35
# time = 3
# speed = distance / time
# print(f"Biegasz z prędkością średnią: {speed: .2f} km/h")

# zadanie domowe typ str
# start_value = input("Podaj poczatkowa wartosc lokaty (zl): ")
# percent = input("Podaj oprocentowanie lokaty (%): ")
# duration = input("Poda czas trwania (lata): ")
#
# value = float(start_value) * (1 + float(percent) / 100) ** int(duration)
# print(f"Wartosc lokaty po {duration} latach bedzie wynosila:{value: .2f} zl")
#
# name = input("Podaj swoje imie: ")
# print(f"Twoje imie ma {len(name)} liter.")

# city = input("Gdzie mieszkasz? ")
# print(f"To milo, ze mieszkasz w {city.title()}!")

# ford = "ab100100"
# audi = "EEE 123123"
# citroen = "Zk-300300"
# honda = "AB210210"
#
# ford = ford.upper()
# audi = audi.replace(' ', '')
# citroen = citroen.upper().replace('-', '')
# print(f"Poprawne dane samochodow: {ford}, {audi}, {citroen}, {honda}.")

# favourite_flavours = [
#     "malinowy",
#     "truskawkowy",
#     "czekoladowy",
#     "pistacjowy",
#     "kokosowy"
# ]
# # print("dwa najbardziej ulubione smaki: ", favourite_flavours[:2])
# # print("wszystkie smaki poza ulubionymi: ", favourite_flavours[2:])
# # print("Dwa najmniej ulubione smaki: ", favourite_flavours[-2:])
#
# # dodanie elementu na koncu listy
# favourite_flavours.append("kawowy")
# print(favourite_flavours)
#
# # dodanie elementu w dowolnym miejscu listy
# favourite_flavours.insert(0, "jagodowy")
# print(favourite_flavours)
#
# # usuniecie po indeksie
# del favourite_flavours[4]
# print(favourite_flavours)
#
# # wyciagniecie elementu z listy
# second_flavour = favourite_flavours.pop(1)
# print(second_flavour)
# print(favourite_flavours)
#
# # usuniecie po wartosci
# favourite_flavours.remove("czekoladowy")
# print(favourite_flavours)
#
# # podmiana elementu
# favourite_flavours[-1] = "malinowy"
# print(favourite_flavours)

# favourite_sport = [
#     "tenis stołowy",
#     "tenis ziemny",
#     "piłka nożna",
#     "koszykówka",
#     "kolarstwo"
# ]
# print("Najlepszy sport: ", favourite_sport[0])
# print("Najbardziej nielubiany sport to: ", favourite_sport[-1])
# favourite_sport[-1] = "siatkówka"
# print(favourite_sport)

# favourite_food = []
#
# for i in range(3):
#     food = input(f"Podaj potrawe nr {i+1}: ")
#     favourite_food.append(food)
# print(favourite_food)

# phone_number = input("Podaj nr telefonu: ")
# public_digits = phone_number[:6]
# number_of_private_digits = len(phone_number) - 6
# private_digits = '-' * number_of_private_digits
# anonymous_number = public_digits + private_digits
# print(anonymous_number)

# słowniki
# słownik polsko-angielski
# polish_to_english = {
#     "amnezja": "amnesia",
#     "aktywista": "activist",
#     "burza": "storm"
# }
#
# print(f"Po polsku 'burza' to po angielsku: '{polish_to_english['burza']}'")
#
# # pusty slownik
# empty = {}
# print("Pusty slownik: ", empty)
#
# # wartości mogą być różnych typów
# expedintures = {
#     "prąd": 250,
#     "woda": 30.45,
#     "zakupy": [
#         120.15,
#         170.53,
#         20.15
#     ]
# }
# print(expedintures)

# dobrą praktyką jest stosowanie jednej konwencji czyli np. jak niżej zrobienie z wartości jednoelementowych list :-)
# expedintures = {
#     "prąd": [250],
#     "woda": [30.45],
#     "zakupy": [
#         120.15,
#         170.53,
#         20.15
#     ]
# }
# print(expedintures)
#
# # typ int oraz float też mogą być kluczem
# expedintures = {
#     250: "prąd",
#     30.45: "woda",
#     120.15: "zakupy",
#     170.53: "zakupy",
#     20.15: "zakupy"
# }
# print(expedintures)

# wartości mogą się powatarzać w słowniku ale klucze nie, przykład niżej
# expedintures = {
#     250: "prąd",
#     30.45: "woda",
#     250: "zakupy"
# }
# print(expedintures) # nie pokaże zakupów bo taka wartość już istnieje i jest przypisana do innej wartości (nie bedzie prądu bo # nadpiszą go zakupy)

# słowniki mogą zawierać inne słowniki
# teacher = {
#     "first_name": "Jan",
#     "last_name": "Kowalski",
#     "age": 45,
#     "contract": {
#         "sign_date": "23-11-2018",
#         "salary": 3500
#     }
# }
# print(teacher)
#
# # jak słownik może zawierać listy, tak lista może zawierać słownik
# students = [
#     {
#         "first_name": "Patryk",
#         "last_name": "Nowak",
#     },
#     {
#         "first_name": "Alicja",
#         "last_name": "Kowalska",
#     }
# ]
# print(students)
# print(students[0])
# print(students[1])
# print(students[1]['first_name'])

# teacher = {
#     "first_name": "Jan",
#     "last_name": "Kowalski",
#     "age": 45,
#     "contract": {
#         "sign_date": "23-11-2018",
#         "salary": 3500
#     }
# }
# teacher["first_name"] = "Albert"
# teacher["city"] = "Gdańsk"
# # del teacher["last_name"]
# print(teacher["car"])
# print(teacher)

# # metody słownika - wyciągniecie elementu po kluczu
# teacher = {
#     "first_name": "Jan",
#     "last_name": "Kowalski",
#     "age": 45,
#     "contract": {
#         "sign_date": "23-11-2018",
#         "salary": 3500
#     }
# }
# age = teacher.pop("age")
# print(age)
# print(teacher)

# metody keys oraz values zwracają obiekty specjalnych typów
# Reprezentujące klucze oraz wartości w słowniku
# teacher = {
#     "first_name": "Jan",
#     "last_name": "Kowalski",
#     "age": 45,
#     "contract": {
#         "sign_date": "23-11-2018",
#         "salary": 3500
#     }
# }
# print(teacher.keys())
# print(teacher.values())
#
# # za pomocą funkcji list() możemy zmienić te typy na listę kluczy i wartości
# keys = list(teacher.keys())
# values = list(teacher.values())
# print(keys)
# print(values)
#
# # funkcja len na słowniku zwraca nam liczbę elementów (kluczy) w słowniku
# print(len(teacher))

# school_grades = {
#     "matematyka": [5, 3, 2, 5, 4],
#     "biologia": [2, 3, 5, 4],
#     "fizyka": [5, 5, 4, 2, 5],
#     "język angielski": [5, 5, 5, 3, 5]
# }
# print("oceny w szkole:", school_grades)
#
# my_family = {
#     "first_name": "Piotr",
#     "last_name": "Burek",
#     "birth_date": "05-05-1985",
#     "parents": [
#         {
#             "first_name": "Jozef",
#             "last_name": "Burek",
#             "birth_date": "30-11-1957",
#             "parents": [
#                 {
#                     "first_name": "Bronislaw",
#                     "last_name": "Burek",
#                     "birth_date": "08-06-1912",
#                     "parents": [],
#                 },
#                 {
#                     "first_name": "Anna",
#                     "last_name": "Burek",
#                     "birth_date": "08-07-1912",
#                     "parents": [],
#                 },
#             ]
#         },
#         {
#             "first_name": "Zenobia",
#             "last_name": "Burek",
#             "birth_date": "13-11-1932",
#             "parents": [
#                 {
#                     "first_name": "Zofia",
#                     "last_name": "Burek",
#                     "birth_date": "06-06-1944",
#                     "parents": [],
#                 },
#                 {
#                     "first_name": "Anna",
#                     "last_name": "Kuras",
#                     "birth_date": "15-11-1931",
#                     "parents": [],
#                 },
#             ]
#         }
#     ],
# }
# print("drzewo genealogiczne", my_family)

# print("ile przez miesiac wydajesz na: ")
# food = float(input("Jedzenie? "))
# fun = float(input("Rozrywkę? "))
# bills = float(input("Opłaty? "))
# other = float(input("Inne? "))
#
# total_expedintures = food + fun + bills + other
#
# expedintures_percentage = {
#     "jedzenie": food * 100 / total_expedintures,
#     "rozrywka": fun * 100 / total_expedintures,
#     "opłaty": bills * 100 / total_expedintures,
#     "inne": other * 100 / total_expedintures
# }
#
# choice = input("Wybierz jedna z kategorii (jedzenie/rozrywka/opłaty/inne): ")
# print(f"Na {choice} wydajesz {expedintures_percentage[choice]:.0f}%")

# lekcja typ None
# nothing = None
# # None ma typ NoneType
# print(f"None jest typu: {type(None)}")

# None możemy użyć jako wartość w słowniku
# people = [
#     {
#         "first_name": "Alicja",
#         "car": {
#             "brand": "Ford",
#             "production_year": 2015
#         }
#     },
#     {
#         "first_name": "Jakub",
#         "car": None
#     }
# ]
# print(people)

# None może być elementem na liście
# something = [1, 4, 6, None, 8]
# print(something)
#
# # Na None nie możemy wykonywać operacji arytmetycznych, łączyć bezpośrednio z napisami itd.
# wrong = 3 + None
# wrong = "Napis" + None

# Nie możemy zamienić None na liczbę ani na listę
# wrong = int(None)
# wrong = float(None)
# wrong = list(None)

# None kowertuje się na stringa jako napis "None"
# none_str = str(None)
# print(none_str)