# pętla while
# counter = 0
# while counter <= 30:
#     print(counter)
#     counter += 1
#
# while True:
#     print("Nigdy nie skończę!!!")

# expected_potatoes = int(input("Ile ziemniaków chcesz na obiad? "))
# potatoes = []
# while len(potatoes) < expected_potatoes:
#     print("Obieram ziemniaka...")
#     print("I wrzucam do garnka")
#     potatoes.append("Ziemniak")
# print(potatoes)

# chcemy żeby liczba podana przez użytkownika była większa niż 100
# number = 0
# while number <= 100:
#     number = int(input("Podaj liczbę większą niż 100: "))
#     if number <= 100:
#         print(f"{number} nie jest większe niż 100. Spróbujmy jeszcze raz... \n")
#
# print(f"Brawo!")

# możemy upewnić się, że użytkownik podał sesnowną wartość
# age = int(input("Ile masz lat? "))
# while age < 1:
#     if age < 1:
#         print("Chyba nie... \n")
#         age = int(input("Ile masz lat? "))
#
# if age < 18:
#     print("Jeszcze nie możesz głosować")
# else:
#     print("Możesz już głosować!")

# Pozwalamy użytkownikowi skorzystać z programu wielokrotnie
# option = "T"
# while option.upper() == "T":
#     income = int(input("Podaj przychód: "))
#     employees_number = int(input("Podaj liczbę pracowników: "))
#     years_on_the_market = int(input("Ile lat działacie na rynku: "))
#     if income < 2000:
#         print("Przyznano główne wsparcie")
#     elif 5 <= employees_number <= 10:
#         print("Przyznano wsparcie z funduszu pracowników")
#     elif years_on_the_market < 3:
#         print("Przyznano wsparcie dlan nowych firm")
#     else:
#         print("Przyznano wsparcie na pocieszenie ;)")
#
#     option = input("Jeżeli chcesz sprawdzić dla innych danych wpisz 'T': ")

# favourite_sports = ["bieganie", "pływanie", "jazda na rowerze", "triathlon"]
# sport_index = 0
# while sport_index < len(favourite_sports):
#     print(favourite_sports[sport_index])
#     sport_index += 1

# wypisujemy kod pocztowy - znak po znaku
# post_code = input("Jaki jest Twój kod pocztowy? ")
# letter_index = 0
# while letter_index < len(post_code):
#     print(f"{letter_index} -> {post_code[letter_index]}")
#     letter_index += 1

# Zamieniamy kod pocztowy by był zgodny z formatem XX-XX-XX-XX...
# post_code = input("Jaki jest Twój kod pocztowy? ")
# post_code = post_code.replace('-', '')
# formatted_post_code = ""
# letter_index = 0
# while letter_index < len(post_code):
#     if letter_index % 2 == 0 and letter_index != 0:
#         formatted_post_code += '-'
#     formatted_post_code += post_code[letter_index]
#     letter_index += 1
# print(formatted_post_code)

# zadanie nr 1
# print("Masz 10 prób!")
# number = int(input("Podaj liczbę: "))
# counter = 0
# while counter < 11:
#     if number % 2 != 0:
#         number = int(input("podaj liczbę: "))
#     else:
#         print("Podałeś parzystą liczbę!")
#         break
#     counter += 1
# print("Czybys podal parzysta liczbę albo nie podałeś jej wcale?")

# zadanie nr 2 - rozwiązanie Mikołaja
# number = int(input("Podaj liczbę parzystą: "))
# try_number = 1
# while try_number < 10 and number % 2 != 0:
#     number =int(input("Spróbuj jeszcze raz! Podaj liczbę parzystą: "))
#     try_number += 1

# zadanie nr 2
# phone_number = input("Podaj nr telefonu: ")
# phone_number = phone_number.replace('-', '')
# formatted_phone_number = ""
# number_index = 0
# while number_index < len(phone_number):
#     if number_index % 3 == 0 and number_index != 0:
#         formatted_phone_number += '-'
#     formatted_phone_number += phone_number[number_index]
#     number_index += 1
# print(formatted_phone_number)

# zadanie nr 3
# favourite_dishes = input("Podaj swoje ulubione dania (oddziel je przecinkiem): ")
# favourite_dishes = favourite_dishes.split(',')
# dish_index = 0
# while dish_index < len(favourite_dishes):
#     print(f"Miejsce {dish_index+1} zajmuje: {favourite_dishes[dish_index]}")
#     dish_index += 1

# lekcja pętla for
# collection = ["ciastko", "książka", "wielkie NIC"]
# for element in collection:
#     print(element)

# wypisywanie listy ulubionych sportów
# favourite_sports = ["bieganie", "pływanie", "jazda na rowerze"]
# for sport in favourite_sports:
#     print(sport)

# kod pocztowy po znaku
# post_code = input("Jaki jest Twój kod pocztowy: ")
# for letter in post_code:
#     print(letter)

# za pomocą pętli wypisać klucze ze słownika:
# expenditures = {
#     "prąd": [250],
#     "woda": [30.45],
#     "zakupy": [
#         120.15,
#         170.33,
#         20.15
#     ]
# }
# for expenditure_name in expenditures:
#     print(expenditure_name)
#
# # klucze i wartości:
# for expenditure_name in expenditures:
#     print(f"{expenditure_name} => {expenditures[expenditure_name]}")
#
# # wartości
# for expenditure in expenditures.values():
#     print(expenditure)
#
# # klucze i wartości bezpośrednio
# for expenditure_name, expenditure in expenditures.items(): # rozpakowywanie słownika
#     print(f"{expenditure_name} => {expenditure}")
#
# for item in expenditures.items():
#     print(item)
#     print(f"{item[0]} => {item[1]}")
# print(type(item))

# nie można zmodyfikowac krotki
# item = ("prąd", 340)
# item[1] = 20

# kroktę można rozpakować
# item = ("prąd", 340)
# name, value = item
# print(name, value)

# enumerate - daje index, wartość gdy potrzebujemy
# wypisujemy kod pocztowy - znak po znaku
# post_code = input("Jaki jest Twój kod pocztowy: ")
# for index, letter in enumerate(post_code):
#     print(f"[{index}] => {letter}")

# wypisywanie co drugiego sportu
# favourite_sports = ["bieganie", "pływanie", "jazda na rowerze"]
# for index, sport in enumerate(favourite_sports):
#     if index % 2 == 0:
#         print(sport)

# zmieniamy kod pocztowy by zawsze był zgodny z formatem XX-XX-XX...
# post_code = input("Jaki jest Twój kod pocztowy: ")
# post_code = post_code.replace('-', '')
# formatted_post_code = ""
# for index, digit in enumerate(post_code):
#     if index % 2 == 0 and index != 0:
#         formatted_post_code += '-'
#     formatted_post_code += digit
# print(formatted_post_code)

# zadanie nr 1
# total_sum = 0
# amount_of_numbers = 0
# text = input("Podaj kolejne oceny oddzielając je przecinkiem: ")
# text = text.split(',')
# for number in text:
#     total_sum += int(number)
# amount_of_numbers = len(text)
# average = total_sum / amount_of_numbers
# print(f"Średnia ocen wynosi: {average:.2f}")

# zadanie nr 1 rozwiązanie Mikołaja
# grades = []
# grade_input = input("Podaj kolejną ocenę albo zakończ wpisując 'X': ")
# while grade_input.upper() != 'X':
#     grade = int(grade_input)
#     grades.append(grade)
#     grade_input = input("Podaj kolejną ocenę albo zakończ wpisując 'X': ")
#
# grades_sum = 0
# for grade in grades:
#     grades_sum += grade
#
# average = grades_sum / len(grades)
# print(f"Twoja średnia wynosi: {average:.2f}")

# zadanie nr 2
# phone_number = input("Podaj nr telefonu: ")
# phone_number = phone_number.replace('-', '')
# formatted_phone_number = ""
#
# for number_index, number in enumerate(phone_number):
#     if number_index % 3 == 0 and number_index != 0:
#         formatted_phone_number += '-'
#     formatted_phone_number += phone_number[number_index]
# print(formatted_phone_number)

# zadanie nr 3
# option = 'T'
# expenditures = {}
#
# while option.upper() == 'T':
#     for expend in expenditures:
#         expend = input("Podaj nazwe wydatku: ")
#         expenditures[expend] = float(input("Podaj wartość wydatków: "))
#     print(expenditures)
#     option = input("czy chcesz jeszcze raz wprowadzić dane: ")

# zadanie nr 3 rozwiązanie Mikołaja
# print("Kalkulator budżetu miesięcznego: ")
# expenditures = {}
# category_name = input("Podaj kategorię wydatków albo zakończ wpisując 'X': ")
# while category_name.upper() != 'X':
#     expenditures[category_name] = []
#     expenditure = input(f"Podaj wartość następnego wydatku w kategorii {category_name} albo zakończ wpisując 'X': ")
#     while expenditure.upper() != 'X':
#         expenditure_value = float(expenditure)
#         expenditures[category_name].append(expenditure_value)
#         expenditure = input(f"Podaj wartość następnego wydatku w kategorii {category_name} albo zakończ wpisując 'X': ")
#     category_name = input("Podaj kategorię wydatków albo zakończ wpisując 'X': ")
# total_expenditures = 0
# for category_expenditures in expenditures.values():
#     for expenditure_value in category_expenditures:
#         total_expenditures += expenditure_value
#
# expenditures_percentage = {}
# for category_name, category_expenditures in expenditures.items():
#     total_category_expenditures = 0
#     for expenditure_value in category_expenditures:
#         total_category_expenditures += expenditure_value
#     expenditures_percentage[category_name] = total_category_expenditures * 100 / total_expenditures
#
# most_important_category = None
# most_important_category_percentage = 0
# for category, percentage in expenditures_percentage.items():
#     if percentage > most_important_category_percentage:
#         most_important_category_percentage = percentage
#         most_important_category = category_name
#
# if most_important_category is not None:
#     print(f"Najwięcej wydajesz na {most_important_category} - {most_important_category_percentage:.0f}%")
# for category, percentage in expenditures_percentage.items():
#     print(f"Na {category} wydajesz {percentage:.0f}% miesięcznie")

# lekcja pętla for in range
# expenditures = {}
# category_name = input("Podaj nazwę kategorii lub  zakończ wpisując 'X': ")
# while category_name.upper() != 'X':
#     expenditures[category_name] = []
#     expenditure = input(f"Podaj wydatki kategorii {category_name} albo zakończ wpisując 'X': ")
#     while expenditure.upper() != 'X':
#         expenditure_value = float(expenditure)
#         expenditures[category_name].append(expenditure_value)
#         expenditure = input(f"Podaj wartość kolejnego wydatku albo zakończ wpisując 'X': ")
#     category_name = input("Podaj nazwę kolejnej kategorii lub zakończ wpisując 'X': ")
# print(expenditures)
# total_expenditures = 0
# for category_expenditures in expenditures.values():
#     for category_value in category_expenditures:
#         total_expenditures += category_value
# print(total_expenditures)
#
# expenditures_percentage = {}
# for category_name, category_expenditures in expenditures.items():
#     total_category_expenditures = 0
#     for category_value in category_expenditures:
#         total_category_expenditures += category_value
#     expenditures_percentage[category_name] = total_category_expenditures * 100 / total_expenditures
# print(expenditures_percentage)
#
# most_important_category = None
# most_important_category_percentage = 0
# for category, percentage in expenditures_percentage.items():
#     if percentage > most_important_category_percentage:
#         most_important_category = category
#         most_important_category_percentage = percentage
# if most_important_category is not None:
#     print(f"Najwiecej wydajesz na {most_important_category} co stanowi {most_important_category_percentage:.0f}% całkowitych wydatków!")
# for category, percentage in expenditures_percentage.items():
#     print(f"Na {category} wydajesz {percentage:.0f}% miesięcznie.")

# lekcja pętla for in range
# wypisywanie kolejnych liczb
# for number in range(12):
#     print(number)
#
# # zaczynamy od 1 do 12
# for number in range(1, 13):
#     print(number)

# od 1, co trzecia liczba
# for number in range(1, 13, 3):
#     print(number)

# print("Kalkulator wartości lokaty z roczną kapitalizacją")
#
# initial_value_input = input("Jaką kwotę wpłaciłeś/wpłaciłaś? ")
# initial_value = int(initial_value_input)
# percentage_input = input("Jakie jest oprocentowanie (?)? ")
# percentage = int(percentage_input)
# years_input = input("Ile lat trwa lokata? ")
# years = int(years_input)
#
# for year_number in range(1, years + 1):
#     investment_value = initial_value * (1 + percentage / 100) ** year_number
#     print(f"Po {year_number} latach Twoja lokata będzie warta {investment_value:.2f} zł")

# metoda count - zwraca liczbę wystąpień danego znaku w napisie
# sentence = "Napis z dużą liczbą aaa"
# print(sentence.count('a'))

# zadanie nr 1
# phone_number = input("Podaj nr telefonu: ")
# for digit in range(10):
#     appearances_digits_in_phone_number = phone_number.count(str(digit))
#     print(f"Cyfra {digit} występuje {appearances_digits_in_phone_number} raz(y)")

# zadanie nr 2
# credit_value = float(input("Podaj kwotę kredytu: "))
# credit_interest = float(input("Podaj oprocentowanie kredytu (stałe)%: "))
# duration = int(input("Podaj czas trwania w latach: "))
# additional_costs = float(input("Podaj koszty początkowe (np. prowizje itp.): "))
#
# monthly_paid_capital = credit_value / (duration * 12)
# months = duration * 12
# for month in range(1, months + 1):
#     remaining_capital = credit_value - (month - 1) * monthly_paid_capital
#     installment = (remaining_capital * credit_interest / 100) / 12 + monthly_paid_capital
#     total_paid += installment
#     print(f"{remaining_capital:.2f}")

# zadanie nr 2 rozwiązanie Mikołaja
# capital = int(input("Na jaką kwotę jest kredyt: "))
# interest_rate = float(input("Jakie jest oprocentowanie (%): "))
# years = int(input("Na ile lat jest kredyt: "))
# initial_fees = int(input("Jakie są koszty początkowe: "))
#
# credit_time_in_months = years * 12
# monthly_paid_capital = capital / credit_time_in_months
# total_paid = initial_fees
# for month_number in range(1, credit_time_in_months + 1):
#     capital_to_be_paid = capital - (month_number - 1) * monthly_paid_capital
#     installment = (capital_to_be_paid * interest_rate / 100) / 12 + monthly_paid_capital
#     total_paid += installment
#     print(f"Rata w miesiacu {month_number} wyniesie {installment} zł.")
#
# print(f"Zaciągając {capital} na tych warunkach spłacisz {total_paid:.2f}")

# lekcja komendy break i continue
# expenditures = [120, 300, 250.45, 1300, 50, 75]
#
# for expenditure in expenditures:
#     if expenditure > 1000:
#         print("Drogi wydatek znaleziony!")
#         break
#
# grades = []
# while True:
#     grade_input = input("Podaj kolejną ocenę albo zakończ wpisując 'X': ")
#     if grade_input.upper() == 'X':
#         break
#     grade = int(grade_input)
#     grades.append(grade)
#
# grades_sum = sum(grades)
# average = grades_sum / len(grades)
# print(f"Twoja średnia wynosi: {average:.2f}")

# również pętla while ma opcjonalnego else'a
# grades = []
# while len(grades) < 5:
#     grade_input = input("Podaj kolejną ocenę albo zakończ wpisując 'X': ")
#     if grade_input.upper() == 'X':
#         break
#     grade = int(grade_input)
#     grades.append(grade)
# else:
#     print("Wystarczy już tych ocen!")
#
# grades_sum = sum(grades)
# average = grades_sum / len(grades)
# print(f"Twoja średnia wynosi: {average:.2f}")

# wypisywanie co drugiego sportu z listy
# favourite_sports = ["bieganie", "pływanie", "jazda na rowerze", "triathlon"]
# for index, sport in enumerate(favourite_sports):
#     if index % 2 != 0:
#         continue
#     print(sport)

# zadanie nr 1
# grades = input("Podaj kolejne oceny oddzielając je przecinkiem: ")
# grades = grades.split(',')
# passing_flag = True
# for grade in grades:
#     if int(grade) == 1:
#         passing_flag = False
#         break
# if passing_flag == True:
#     print("Zdałeś/aś do następnej klasy :)")
# else:
#     print("Niestety ale nie zdałeś/aś do następnej klasy :(")
# rozwiązanie Mikołaja
# subjects = ["matematyka", "fizyka", "język polski", "język angielski", "historia"]
# grades = []
# for subject in subjects:
#     grade = int(input(f"Jaka jest Twoja ocena z przedmiotu {subject}: "))
#     grades.append(grade)
# for grade in grades:
#     if grade == 1:
#         print("Niestety...")
#         break
# else:
#     print("Gratuluję! Zdałeś/aś do następnej klasy :)")

# zadanie nr 2
# print("Kalkulator miesięcznego budżetu :)")
# expenditures = {}
# category_name = input("Podaj kategorię wydatków albo zakończ wpisując 'X': ")
#
# while category_name.upper() != 'X':
#     expenditures[category_name] = []
#     expenditure = input(f"Podaj wartość następnego wydatku w kategorii {category_name} lub zakończ wpisując 'X': ")
#     while expenditure.upper() != 'X':
#         expenditure_value = float(expenditure)
#         expenditures[category_name].append((expenditure_value))
#         expenditure = input(f"Podaj wartość kolejnego wydatku w kategorii {category_name} lub zakończ wpisując 'X': ")
#     category_name = input("Podaj kolejną kategorię wydatków lub zakończ wpisując 'X': ")
#
# total_expenditures = 0
# for category_name in expenditures.values():
#     for expenditure in category_name:
#         total_expenditures += float(expenditure)
# print(total_expenditures)

# rozwiązanie Mikołaja
# print("Kalkulator miesięcznego budżetu :)")
# expenditures = {}
#
# while True:
#     category_name = input("Podaj kategorię wydatków albo zakończ wpisując 'X': ")
#     if category_name.upper() == 'X':
#         break
#     expenditures[category_name] = []
#
#     while True:
#         expenditure = input(f"Podaj wartość następnego wydatku w kategorii {category_name} lub zakończ wpisując 'X': ")
#         if expenditure.upper() == 'X':
#             break
#
#         expenditure_value = float(expenditure)
#         expenditures[category_name].append((expenditure_value))
#
# total_expenditures = 0
# for category_name in expenditures.values():
#     # total_expenditures += sum(category_name)
#     for expenditure in category_name:
#         total_expenditures += float(expenditure)
#
# expenditures_percentage = {}
# for category_name, category_expenditures in expenditures.items():
#     total_category_expenditures = sum(category_expenditures)
#     expenditures_percentage[category_name] = total_category_expenditures * 100 / total_expenditures
#
# most_important_category = None
# most_important_category_percentage = 0
# for category, percentage in expenditures_percentage.items():
#     if percentage > most_important_category_percentage:
#         most_important_category = category
#         most_important_category_percentage = percentage
#
# if most_important_category is not None:
#     print(f"Najwięcej wydajesz na {most_important_category} i jest to {most_important_category_percentage:.0f}% całkowitych wydatków!")
# for category, percentage in expenditures_percentage.items():
#     print(f"Na {category} wydajesz {percentage:.0f}% całkowitych wydatków!")

# zadanie nr 3
# number_input = input("Podaj liczbę albo zakończ wpisując 'X': ")
# numbers = []
# while number_input.upper() != 'X':
#     numbers.append(number_input)
#     number_input = input("Podaj kolejną liczbę albo zakończ wpisując 'X': ")
# for number in numbers:
#     if int(number) % 2 == 0:
#         continue
#     print(number)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for name in student_marks:
        if name == query_name:
            avg_value = sum(student_marks[name]) / len(student_marks[name])
    print(f"{avg_value:.2f}")

