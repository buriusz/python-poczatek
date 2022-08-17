# # Instrukcje warunkowe i petle
# result = bool(7)
# print("bool(7):", result)
# print("bool(\"Napis\"):", bool("Napis"))
#
# # Porównując dwie wartości musimy wiedzieć co Python porównuje
# # w przypadku słów porównuje czy litery sa później w alfabecie
# # jak są później to ta wartość jest większa
# print(f"Warzywa > Słodycze -> {'Warzywa'  > 'Słodycze'}")
#
# # Taki zapis nie jest zbyt czytelny
# shopping_list = ["Mąka", "Jogurt"]
# my_list = ["Czekolada", "Marchewka", "Chleb"]
# print(f"{shopping_list} > {my_list} -> {shopping_list > my_list}")

# zadanie
# flour = float(input("Podaj cene mąki: "))
# candies = float(input("Podaj cenę cukierków: "))
# ice_cream = float(input("Podaj cenę lodów: "))
#
# print(f"mąka < cukierki -> {flour < candies}")
# print(f"mąka > cukierki -> {flour > candies}")
# print(f"cukierki < lody -> {candies < ice_cream}")
# print(f"cukierki > lody -> {candies > ice_cream}")
# print(f"mąka < lody -> {flour < ice_cream}")
# print(f"mąka > lody -> {flour > ice_cream}")

# shopping_elements = input("Wprowadz liste zakupow oddzielając je przecinkami: ")
# shopping_list = shopping_elements.split(',')
# print(shopping_list)
# is_shopping_list_long = len(shopping_list) > 6
# print(f"Czy uważam, że Twoja lista zakupów jest duża - {is_shopping_list_long}")
#
# start_value = input("Podaj poczatkowa wartosc lokaty (zl): ")
# percent = input("Podaj oprocentowanie lokaty (%): ")
# duration = input("Poda czas trwania (lata): ")
#
# value = float(start_value) * (1 + float(percent) / 100) ** int(duration)
# profit_percentage = ((value-float(start_value))*100/float(start_value)) >= 10
# print(f"Czy wartość lokaty wzrośnie o co najmniej 10% w żądanym okresie? - {profit_percentage}")
# print(f"Wartosc lokaty po {duration} bedzie wynosila: {value} zl")

# lekcja
# if 7 > 3:
#     print("To oczywiste!")
#
# if 10 < 4:
#     print("To sie nigdy nie zdarzy!")
#
# age = int(input("Ile masz lat? "))
# if age < 18:
#     print("Jeszcze nie mozesz glosowac!")
# if age >= 18:
#     print("Mozesz juz glosowac!")

# przyklad z if wzbogacony o else
# if 7 > 3:
#     print("To oczywiste!")
# else:
#     print("To sie nie wydarzy!")

#zadanie
# flour = float(input("Podaj cene mąki: "))
# candies = float(input("Podaj cenę cukierków: "))
# ice_cream = float(input("Podaj cenę lodów: "))
#
# if flour <= candies:
#     print("Cena mąki jest mniejsza lub równa cenie cukierków")
# else:
#     print("Cena mąki jest większa od ceny cukierków")
#
# if flour <= ice_cream:
#     print("Cena mąki jest mniejsza lub równa cenie lodów")
# else:
#     print("Cena mąki jest większa od ceny lodów")
#
# if candies <= ice_cream:
#     print("Cena cukierków jest mniejsza lub równa cenie lodów")
# else:
#     print("Cena cukierków jest większa od ceny lodów")
#
# print("Ile wydajesz na (wypisz kwoty oddzielając je przecinkiem: ")
# food = float(input("jedzenie: "))
# fun = float(input("rozrywkę: "))
# bills = float(input("rachunki: "))
# other = float(input("inne: "))
#
# total_expedintures = food + fun + bills + other
# expedintures = {
#     "jedzenie": food * 100 / total_expedintures,
#     "rozrywka": fun * 100 / total_expedintures,
#     "rachunki": bills * 100 / total_expedintures,
#     "inne": other * 100 / total_expedintures
# }
# maximum = max(expedintures.values())
#
# print(f"Najwiekszy udzial w wydatkach wynosi {maximum}%")
# print(expedintures(maximum))

# math_ = input("Podaj oceny z matematyki (oddziel je przecinkiem): ")
# math_ = math_.split(',')
# biology = input("Podaj oceny z biologii: ")
# biology = biology.split(',')
# english = input("Podaj oceny z jezyka angielskiego: ")
# english = english.split(',')
# passed = True
# for m in math_:
#     if int(m) == int(1):
#         passed = False
# if passed:
#     print("Chyba zdałeś/łaś matematykę")
# else:
#     print("Chyba nie zdałeś/łaś matematyki")
#
# passed = True
# for biol in biology:
#     if int(biol) == int(1):
#         passed = False
# if passed:
#     print("Chyba zdałeś/łaś biologię")
# else:
#     print("Chyba nie zdałeś/łaś biologii")
#
# passed = True
# for eng in english:
#     if int(eng) == int(1):
#         passed = False
# if passed:
#     print("Chyba zdałeś/łaś angielski")
# else:
#     print("Chyba nie zdałeś/łaś angielskiego")




# name = input("Podaj imie: ")
# if name.endswith('a'):
#     print("Jestes kobieta!")
# else:
#     print("Nie jestes kobieta!")

# if name[-1] == 'a':
#     print("Jestes kobieta!")
# else:
#     print("Nie jestes kobieta!")

# lekcja
# dość skomplikowane rozwiązanie
# name = input("Jak się nazywasz? ")
# print(f"Miło Cie poznać {name}")
# name_length = len(name)
#
# if name_length < 5:
#     print(f"{name} to raczej krótkie imię.")
# if name_length >= 5:
#     if name_length <= 8:
#         print(f"{name} to imię zwykłej długości")
#     else:
#         print(f"{name} to długie imię")
# uproszczone rozwiązanie
# name = input("Jak się nazywasz? ")
# print(f"Miło Cie poznać {name}")
# name_length = len(name)
# if name_length < 5:
#     print(f"{name} to raczej krótkie imię.")
# if name_length >= 5 and name_length <= 8:
#     print(f"{name} to imię zwykłej długości")
# else:
#     print(f"{name} to długie imię")

# skomplikowane rozwiązanie
# born_as_usa_citizen_answer = input("Czy jestes obywtelem USA od urodzenia (T/N): ")
# age = int(input("Ile masz lat? "))
# usa_residence_years = int(input("Ile lat mieszkasz w USA? "))
#
# if born_as_usa_citizen_answer == 'T':
#     born_as_usa_citizen = True
# else:
#     born_as_usa_citizen = False
#
# if born_as_usa_citizen:
#     if age >= 35:
#         if usa_residence_years >= 14:
#             print("Mozesz kandydować")
#         else:
#             print("Nie mozesz kandydowac!")
#     else:
#         print("Nie mozesz kandydować!")
# else:
#     print("Nie możesz kandydować!")

# born_as_usa_citizen_answer = input("Czy jestes obywtelem USA od urodzenia (T/N): ")
# age = int(input("Ile masz lat? "))
# usa_residence_years = int(input("Ile lat mieszkasz w USA? "))
#
# if born_as_usa_citizen_answer.upper() == 'T':
#     born_as_usa_citizen = True
# else:
#     born_as_usa_citizen = False
#
# if born_as_usa_citizen and age >= 35 and usa_residence_years >= 14:
#     print("Możesz kandydować")
# else:
#     print("Nie możesz kandydować!")

# przykład
# income = float(input("Jaki jest miesieczny przychód Twojej firmy: "))
# number_of_employees = int(input("Ilu pracowników zatrudniasz? "))
# if income < 15000 or number_of_employees >= 3:
#     print("Możesz otrzymać dotacje")
# else:
#     print("Niestety nie otrzymasz dotacji")

# przykład
# income = float(input("Jaki jest miesieczny przychód Twojej firmy: "))
# number_of_employees = int(input("Ilu pracowników zatrudniasz? "))
# support_answer = input("Czy Towja firma otrzymała już dotację (T/N): ")
#
# if support_answer.upper() == 'T':
#     support_used = True
# else:
#     support_used = False
#
# if not support_used and (income < 15000 or number_of_employees >= 3):
#     print("Możesz otrzymać dotacje")
# else:
#     print("Niestety nie otrzymasz dotacji")

# uproszczony kalkulator kredytowy
#
# credit_value = float(input("Podaj kwotę jaką chcesz pożyczyć w zł: "))
# percentage = float(input("Podaj oprocentowanie (%): "))
# own_contribiution = float(input("Podaj wartość wkładu własnego (zł): "))
# credit_period = int(input("Podaj czas kredytowania w latach: "))
# month_income = float(input("Podaj przychód miesieczny (zł): "))
# month_expenses = float(input("Podaj sumę wydatków miesięcznych: "))
#
# instalment = (credit_value * percentage / 100) / 12 + credit_value / (credit_period * 12)
# available_funds = month_income - month_expenses
# property_value = own_contribiution + credit_value
#
# print(f"Wartość raty będzie wynosić: {instalment:.2f} zł.")
# print(f"Dostępne środki: {available_funds:.2f} zł.")
# print(f"Wartość nieruchomości: {property_value:.2f} zł.")
#
# if own_contribiution > 0.2 * property_value and (available_funds - instalment) > 1000:
#     print("Mozesz wziąć kredyt!")
# elif 0.1 * property_value <= own_contribiution <= 0.2 * property_value and (available_funds - instalment) > 2000:
#     print("Możesz wziąć kredyt!")
# elif available_funds < 0.1 * property_value:
#     print("Nie możesz wziąć kredytu!")
# else:
#     print("Nie możesz wziąć kredytu!")

# lekcja instrukcja elif
# income = 5000
# employees_number = 7
# years_on_the_market = 3

# if income < 5000:
#     print("Przyznano główne wsparcie")
# else:
#     if 5 <= employees_number <= 10:
#         print("Przyznano wsparcie z funduszu pracowników")
#     else:
#         if years_on_the_market < 3:
#             print("Przyznano wsparcie dla nowych firm")
#         else:
#             print("Przyznano wsparcie na pocieszenie ;)")

# instrukcja elif pozwala powiedzieć "inaczej, jeśli..."
# if income < 5000:
#     print("Przyznano główne wsparcie")
# elif 5 <= employees_number <= 10:
#     print("Przyznano wsparcie z funduszu pracowników")
# elif years_on_the_market < 3:
#     print("Przyznano wsparcie dla nowych firm")
# else:
#     prnit("Przyznano wsparcie na pocieszenie ;)")

# zadanie instrukcja elif
# print("Kalkulator\nWybierz jedną z poniższych opcji:")
# print("1. Kalkulator wartości kredytu.", "2. Kalkulator wartości lokaty.", "3. Wyjście.", sep= "\n")
# choice = input("Wybierz 1, 2 lub 3: ")
#
# if choice == '1':
#     print("Kalkulator wartości kredytu: ")
#     loan_amount = float(input("Podaj kwote kredytu jaka chcesz wziąć (zł): "))
#     interest_rate = float(input("Podaj oprocentowanie kredytu (%): "))
#     own_contribution = float(input("Podaj wartosc wkładu własnego (zł): "))
#     credit_period = int(input("Podaj czas kredytowania (w latach): "))
#     monthly_income = float(input("Podaj wartość przychodu miesięcznego (zł): "))
#     monthly_expedintures = float(input("Podaj wartość miesięcznych wydatków (zł): "))
#
#     installment_value = (loan_amount * interest_rate / 100) / 12 + loan_amount / (credit_period * 12)
#     available_money = monthly_income - monthly_expedintures
#     property_value = own_contribution + loan_amount
#
#     print(f"Rata kredytu będzie wynosić: {installment_value:.2f}")
#     print(f"Dostępne środki wynoszą: {available_money:.2f}")
#     print(f"Wartość nieruchocmości wynosi: {property_value:.2f}")
#
#     if own_contribution >= 0.2 * property_value and available_money - loan_amount >= 1000:
#         print("Można wziąć kredyt!")
#     elif 0.1 * property_value <= own_contribution < 0.2 * property_value and available_money - installment_value >= 2000:
#         print("Można wziąć kredyt!")
#     else:
#         print("Nie można wziąć kredytu!")
# elif choice == 2:
#     # lokata
#     start_value = input("Podaj poczatkową wartosc lokaty (zl): ")
#     percent = input("Podaj oprocentowanie lokaty (%): ")
#     duration = input("Poda czas trwania (lata): ")
#
#     value = float(start_value) * (1 + float(percent) / 100) ** int(duration)
#     # profit_percentage = ((value-float(start_value))*100/float(start_value)) >= 10
#     # print(f"Czy wartość lokaty wzrośnie o co najmniej 10% w żądanym okresie? - {profit_percentage}")
#     print(f"Wartosc lokaty po {duration} bedzie wynosila: {value:.2f} zl")
# else:
#     print("Wyjscie!")
#     exit(0)

# interpretacja wyników testu Coopera
# print("Test Coopera")
# age = int(input("Podaj wiek (w latach): "))
# sex = input("Podaj płeć (m/k): ")
# score = int(input("Podaj wynik: "))
#
# if age == int(8):
#     if sex.lower() == 'k':
#         if score > 2010:
#             print("Bardzo dobry wynik!")
#         elif score > 1670:
#             print("Dobry wynik!")
#         elif score > 1320:
#             print("Średni wynik!")
#         elif score > 990:
#             print("Zly wynik!")
#         else:
#             print("Bardzo zły wynik!")
#     elif sex.lower() == 'm':
#         if score > 2190:
#             print("Bardzo dobry wynik!")
#         elif score > 1810:
#             print("Dobry wynik!")
#         elif score > 1420:
#             print("Średni wynik!")
#         elif score > 1050:
#             print("Zly wynik!")
#         else:
#             print("Bardzo zły wynik!")
# else:
#     print("Coś poszło nie tak! :(")

# lekcja operatory "is" oraz "in"

# zadania z operatorów:
# zadanie nr 1
# shopping_list = input("Podaj liste zakupów (oddziel je przecinkami): ")
# shopping_list = shopping_list.split(',')
# if "chleb" in shopping_list:
#     print("Chleb jest na liście")
# else:
#     print("Chleba nie ma na liście!")
# if "bułki" in shopping_list:
#     print("Bułki są na liście")
# else:
#     print("Bułek nie ma na liście!")

# zadanie nr 2
# phone_number = input("Podaj nr telefonu (bez spacji czy innych znakow): ")
# zero_flag = False
# for digit in phone_number:
#     if digit == '0':
#         zero_flag = True
# if zero_flag:
#     print("Podany nr telefonu zawiera co najmniej jedno '0'")
# else:
#     print("Podany nr telefonu nie ma ani jednego '0'")

# zadanie nr 2 wg Mikołaja
# phone_number = input("Jaki jest Twój nr telefonu: ")
# if '0' in phone_number:
#     print("Twój nr zawiera cyfrę zero :)")
# else:
#     print("W Twoim numerze nie ma cyfry zero :(")

# zadanie nr 3
# value = 10
#
# if value is True:
#     print("Podana wartość to 'True'")
# elif value is False:
#     print("Podana wartość to 'False'")
# elif value is None:
#     print("Podana wartość to 'None'")
# else:
#     print("Podana wartość nie jest ani 'True', ani 'False', ani 'None'")

