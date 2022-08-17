# lekcja nr 1 - funkcje I
# obieranie ziemniaków - definicja funkcji
# def peel_the_potatoes():
#     expected_potatoes = int(input("Ile ziemniakow chcesz na obiad? "))
#     potatoes = []
#     while len(potatoes) < expected_potatoes:
#         print("Obieram ziemniaka...")
#         print("I wrzucam go do garnka :)")
#         potatoes.append("Ziemniak")
#     print(potatoes)
#
# def make_soup():
#     print("Jest zupa!")
#
# # obieranie ziemniaków - wywołanie funkcji
# peel_the_potatoes()
# make_soup()

# def put_a_brick():
#     print('-', sep = '', end='')
#
# # funkcja może wywołać inna funkcję
# def build_a_wall():
#     wall_length = 10
#     for brick in range(wall_length):
#         put_a_brick()
#     print()
#
# build_a_wall()
#
# def build_longer_wall():
#     wall_length = 30
#     for brick in range(wall_length):
#         put_a_brick()
#     print()
#
# build_longer_wall()

# funkcja może przyjmować parametry - widoczne wewnątrz jako zmienne
# def function_with_params(something, something_else):
#     print(something)
#     print(something_else)
#
# function_with_params(1, 4)
# function_with_params("napis", 4)
# list_example = ["Lista", 'z', "elementami"]
# dict_example = {"Klucz": "Wartość"}
# function_with_params(list_example, dict_example)

# Jeżeli funkcja definiuje parametry to muszą one zostać podane
# function_with_params()

# def calculate_investment_value(initial_value, percentage, years):
#     result = initial_value * (1 + percentage / 100) ** years
#     print(f"Po {years} latach Twoja lokata będzie wynosić {result:.2f} zł.")
#
# print("Kalkulator wartości lokaty z roczna kapitalizacją.")
#
# initial_value_input = input("Jaką kwotę wpłaciłeś/aś? ")
# initial_value = float(initial_value_input)
# percentage_input = input("Jakie jest oprocentowanie (%)? ")
# percentage = float(percentage_input)
# years_input = input("Ile lat trwa lokata? ")
# years = int(years_input)
#
# calculate_investment_value(initial_value, percentage, years)

# def calculate_alternative_investment_value(initial_value, percentage, years):
#     result = initial_value * (1 + percentage / 100) ** years
#     print(f"Rozważ zostawienie loakty na {years} lat - wtedy będzie warta {result:.2f}zł.")
# calculate_alternative_investment_value(initial_value, percentage, years * 2)

# def calculate_investment_value(initial_value, percentage, years):
#     result = initial_value * (1 + percentage / 100) ** years
#     return result
#     # return initial_value * (1 + percentage / 100) ** years
#
# print("Kalkulator wartości lokaty z roczna kapitalizacją.")
#
# initial_value_input = input("Jaką kwotę wpłaciłeś/aś? ")
# initial_value = float(initial_value_input)
# percentage_input = input("Jakie jest oprocentowanie (%)? ")
# percentage = float(percentage_input)
# years_input = input("Ile lat trwa lokata? ")
# years = int(years_input)
#
# final_value = calculate_investment_value(initial_value, percentage, years)
# print(f"Po {years} latach Twoja lokata będzie wynosić {final_value:.2f} zł.")
#
# longer_term = years * 2
# alternative_value = calculate_investment_value(initial_value, percentage, longer_term)
# print(f"Rozważ zostawienie lokaty na {longer_term} lat. Wartość lokaty będzie wysoniła {alternative_value:.2f} zł.")

# def say_hello():
#     print("Hello World!")
#     # return None # domyślnie zwraca taką wartość jeśli przypiszemy jak niżej
#
# hello_result = say_hello()
# print(hello_result) # opis jak wyżej - zwróci None :)

# # lekcja nr 2 - funkcje II
# def calculate_investment_value(initial_value, percentage, years):
#     result = initial_value * ( 1 + percentage / 100 ) ** years
#     return result
#
# def ask_for_int_value(message):
#     input_value = input(message)
#     return int(input_value)
#
# def run_investment_calculator():
#     print("Kalkulator wartości lokaty z roczną kapitalizacją")
#
#     initial_value = ask_for_int_value("Jaką kwotę wpłaciłeś/aś (zł)? ")
#     percentage = ask_for_int_value(("Jakie jest oprocentowanie (%)? "))
#     years = ask_for_int_value("Ile lat trwa lokata? ")
#
#     final_value = calculate_investment_value(initial_value, percentage, years)
#     print(f"Po {years} latach Twoja lokata będzie warta {final_value:.2f} zł.")
#
#     longer_term = years * 2
#     alternative_value = calculate_investment_value(initial_value, percentage, longer_term)
#     print(f"Rozważ zostawienie lokaty na {longer_term} lat. Wartość lokaty będzie wtedy wynosiła {alternative_value:.2f} zł.")
#
# option = None
# while option != 'X':
#     run_investment_calculator()
#     option = input("Aby przerwać naciśnij 'X', wpisz inny znak aby kontynuować: ")

# def find_best_grade (grades_by_subject):
#     best_subject = None
#     best_grade = 0
#     for subject, grades in grades_by_subject.items():
#         best_grade_from_subject = max(grades)
#         if best_grade_from_subject > best_grade:
#             best_grade = best_grade_from_subject
#             best_subject = subject
#     return best_grade, best_subject # zapakowanie wyników w krotkę (tuple)
#
# grades_data = {
#     "Historia": [5, 5, 4, 5],
#     "Matematyka": [5, 4, 3, 6],
#     "Fizyka": [4, 3, 2, 5]
# }
# the_best_grade, subject = find_best_grade(grades_data) # rozpakowanie elementów
# print(f"Najlepsza ocena uzyskana to {the_best_grade} z {subject}.")
#
# result = find_best_grade(grades_data)
# print(result)
# print(type(result))

# zadanie nr 1
# def rectangle_area(length, width):
#     return length * width
#
# def ask_for_float_value(message):
#     input_value = input(message)
#     return float(input_value)
#
# length = ask_for_float_value("Podaj długość boku porostokąta (cm): ")
# width = ask_for_float_value("Podaj szerokość boku prostokąta (cm): ")
# area = rectangle_area(length, width)
# print(f"Pole prostokąta wynosi: {area:.2f} cm2.")

# zadanie nr 2
# import sys
# def average_speed(distance, time):
#     if time == 0:
#         print("Niedozwolone działanie / nie wolno dzielić przez '0'!")
#         sys.exit(0)
#     else:
#         average_speed = distance / time
#     return average_speed
#
# def ask_for_float_value(message):
#     input_value = input(message)
#     return float(input_value)
#
#     # print("Kalkulator liczący średnią prędkość biegu, jazdy na rowierze i samochodu (km/h)")
#     # running_distance = ask_for_float_value("Podaj przebiegnięty dystans(km): ")
#     # running_time = ask_for_float_value("Podaj czas biegu(h): ")
#     # bike_ride_distance = ask_for_float_value("Podaj przejechany rowerem dystans(km): ")
#     # bike_ride_time = ask_for_float_value("Podaj czas jazdy rowerem(h): ")
#     # car_drive_distance = ask_for_float_value("Podaj dystans przejechany samochodem(km): ")
#     # car_drive_time = ask_for_float_value("Podaj czas jazdy samochodem(h): ")
#     #
#     # print(f"Średnia prędkość biegu to: {average_speed(running_distance, running_time):.2f} km/h")
#     # print(f"Średnia prędkość na rowerze to: {average_speed(bike_ride_distance, bike_ride_time):.2f} km/h")
#     # print(f"Średnia prędkość samochodu to: {average_speed(car_drive_distance, car_drive_time):.2f} km/h")
#
# # wersja Mikołaja
# def run_average_speed_calculator(vehicle_name):
#     distance = ask_for_float_value(f"Ile km pokonałeś/aś za pomocą {vehicle_name}: ")
#     time = ask_for_float_value("Ile godzin Ci to zajęło: ")
#     avg_speed = average_speed(distance, time)
#     print(f"Twoja średnia prędkość przemieszczania się za pomocą {vehicle_name} wynosiła {avg_speed:.2f}km/h")
#
# run_average_speed_calculator("biegu")
# run_average_speed_calculator("roweru")
# run_average_speed_calculator("samochodu")

# zadanie nr 3
# def load_expenditures(category_name):
#     expenditures_values = []
#     while True:
#         expenditure = input(f"Podaj wartość następnego wydatku {category_name} albo zakończ wpisując 'X': ")
#         if expenditure.upper() == 'X':
#             return expenditures_values
#
#         expenditures_value = float(expenditure)
#         expenditures_values.append(expenditures_value)
#
# def load_expenditures_by_categories():
#     expenditures = {}
#     while True:
#         category_name = input("Podaj kategorię wydatku: ")
#         if category_name.upper() == 'X':
#             return expenditures
#         expenditures[category_name] = load_expenditures(category_name)
#
# def calculate_total_expenditures(expenditures):
#     result = 0
#     for category_expenditures in expenditures.values():
#         result += sum(category_expenditures)
#     return result
#
# def calculate_expenditures_percentages(expenditures, total_expenditures):
#     percentages_by_category_name = {}
#     for category_name, category_expenditures in expenditures.items():
#         total_category_expenditures = sum(category_expenditures)
#         percentages_by_category_name[category_name] = total_category_expenditures * 100 / total_expenditures
#     return percentages_by_category_name
#
# def find_most_important_category(percentages_by_category_name):
#     highest_percentage_category = None
#     highest_percentage = 0
#     for category, percentage in percentages_by_category_name.items():
#         if percentage > highest_percentage:
#             highest_percentage = percentage
#             highest_percentage_category = category
#     return highest_percentage_category, highest_percentage
#
# def print_most_important_category_info(category_name, percentage):
#     print(f"Najwięcej wydajesz na {category_name} - {percentage:.0f}% wszystkich wydatków.")
#
# def print_category_info(category, percentage):
#     print(f"Na {category} wydajesz {percentage:.0f}% miesięcznych wydatków.")
#
# expenditures_by_categories = load_expenditures_by_categories()
# total_expenditures = calculate_total_expenditures(expenditures_by_categories)
# expenditures_percentage = calculate_expenditures_percentages(expenditures_by_categories, total_expenditures)
# most_important_category, most_important_category_percentage = find_most_important_category(expenditures_percentage)
#
# if most_important_category is not None:
#     print_most_important_category_info(most_important_category, most_important_category_percentage)
# for category, percentage in expenditures_percentage.items():
#     print_category_info(category, percentage)

# lekcja argumenty pozycyjne i nazwane
# def add_two_numbers(first_num, second_num):
#     print(f"first_num: {first_num}")
#     print(f"second_num: {second_num}")
#     return first_num + second_num
#
# print(add_two_numbers(2, 5))
# print(add_two_numbers(5, 2))

# nie możemy pomylić kolejności!
# def calculate_investment_value(initial_value, percentage, years):
#     result = initial_value * (1 + percentage / 100)  ** years
#     return result
#
# initial = 1000
# percentage = 5
# years = 4
#
# final_value = calculate_investment_value(percentage, years, initial)
# print(f"Po {years} Twoja lokata będzie wynosić: {final_value:.2f}")
#
# final_value = calculate_investment_value(1000, 5, 4)
# print(f"Po {years} Twoja lokata będzie wynosić: {final_value:.2f}")
#
# def calculate_investment_value(initial_value, percentage, years):
#     result = initial_value * (1 + percentage / 100) ** years
#     return result
#
# final_value = calculate_investment_value(initial_value=1000, percentage=5, years=4)
# print(f"Po {years} Twoja lokata będzie wynosić: {final_value:.2f} zł")

# def calculate_investment_value(initial_value, percentage, years):
#     result = initial_value * (1 + percentage / 100) ** years
#     return result
#
# final_value = calculate_investment_value(initial_value=1000, percentage=5, years=4)
# print(f"Po 4 Twoja lokata będzie wynosić: {final_value:.2f} zł")
#
# # Możemy przekazywać argumenty w dowolnej kolejności
# final_value = calculate_investment_value(percentage=5, years=4, initial_value=1000)
# print(f"Po 4 Twoja lokata będzie wynosić: {final_value:.2f} zł")

# argumenty nazwane powodują dłuższy zapis
# def calculate_investment_value(initial_value, percentage, years):
#     result = initial_value * (1 + percentage / 100) ** years
#     return result
#
# initial = 1000
# percentage = 5
# years = 4
#
# final_value = calculate_investment_value(initial_value=initial, percentage=percentage, years=years)
# print(f"Po {years} Twoja lokata będzie wynosić: {final_value:.2f} zł")
#
# # w jednym wywołaniu możemy łączyć argumenty
# final_value = calculate_investment_value(initial, percentage=percentage, years=years)
# print(f"{final_value:.2f}")

# # argumenty pozycyjne musza być podane w odpowiedniej kolejności przed nazwanymi
# final_value = calculate_investment_value(percentage=percentage, initial, years) # błąd
# print(f"{final_value:.2f}")

# zadanie nr 1
#
# def avg_speed(distance, time):
#     return distance / time
#
# def ask_for_float_value(message):
#     input_value = input(message)
#     return float(input_value)
#
# def run_average_calculator(vehicle_name):
#     distance = ask_for_float_value(f"Podaj dystans w km przebyty za pomocą {vehicle_name}: ")
#     time = ask_for_float_value(f"Podaj czas w h jaki Ci to zajęło: ")
#     average_speed = avg_speed(distance = distance, time = time)
#     print(f"Średnia prędkość {vehicle_name} wyniosła {average_speed:.2f}km/h.")
#
# run_average_calculator(vehicle_name="biegu")

# lecja zakres zmiennych

# def avg_speed(distance, time):
#     result = distance / time
#     print("Nic nie zwracam - ha ha!")
#
# avg_speed(30, 2)
# print(result)

# zmienna distance została zdefiniowana poza jakąkolwiek funkcją - jest globalna
# def avg_speed(time):
#     result = distance / time
#     return result
#
# distance = 20
# time_in_hours = 2
# print(avg_speed(time_in_hours))

# zmienna distance jest zdefiniowana w innej funkcji - jest lokalna i niedostępna
# def avg_speed(time):
#     result = distance / time
#     return result
#
# def calculate_avg_speed():
#     distance = 20
#     time_in_hours = 2
#     print(avg_speed(time_in_hours))
#
# calculate_avg_speed()
# print(distance)

# python przeszukuje zkresy w kolejności: Local -> Enclosing -> Global -> Built in
# jeżeli nie znajdzie definicji symbolu w żadnym z zakresów - mamy błąd

# zmienna nie jest dostępna zanim nie zostanie zdefiniowana
# print(value)
# value = 5
# print(value)

# zmienna musi zostać zdefiniowana zanim wystąpi pierwsze odwołanie do funkcji
# liczy się kolejność wykonania - nie kolejność w skrypcie
# def print_global_name():
#     print(name)
#
# # print_global_name()
# name = "Mikołaj"
# print_global_name()

# zmienna zdefiniowa wewnątrz funkcji
# def failed_modify_global_name():
#     name = "Kuba"
#     print(f"Wewnątrz funkcji: {name}")
#
# name = "Mikołaj"
# print(f"Przed funkcją: {name}")
# failed_modify_global_name()
# print(f"Po funkcji: {name}")

# def success_modify_global_name():
#     global name
#     name = "Kuba"
#     print(f"Wewnątrz funkcji: {name}")
#
# name = "Mikołaj"
# print(f"Przed funkcją: {name}")
# success_modify_global_name()
# print(f"Po funkcji: {name}")

# PI_NUMBER = 3.141
# def circle_area(radius):
#     return PI_NUMBER * radius * radius
#
# print(circle_area(radius=30))

# lekcja parametry domyślne

# def best_grades(grades, best_grades_number = 1):
#     grades.sort(reverse = True)
#     if best_grades_number < len(grades):
#         return grades[:best_grades_number]
#     print("Nie można zwrócić więcej ocen niż jest na liście. Zostaną zwrócone wszystkie...")
#     return grades
#
# math_grades = [1, 3, 4, 1, 2, 5, 4]
# print(best_grades(math_grades))
# print(best_grades(math_grades, 4))
# print(best_grades(math_grades, best_grades_number=4))
#
# # Również funkcja print ma domyślne argumenty
# print("Domyślny", "separator")
# print("Własny", "separator", sep = "---")

# wartości domyślne musza być po wartościach nie domyślnych - inaczej jest błąd jak niżej
# def best_grades(best_grades_number=1, grades):
#     grades.sort(reverse=True)
#     if best_grades_number < len(grades):
#         return grades[:best_grades_number]
#     print("Nie można zwrócić więcej ocen niż jest na liście. Zostaną zwrócone wszystkie...")
#     return grades

# uwaga! Jeżeli jako domyślnego argumentu chcemy użyć Listy lub Słownika
# należy to zrobić w ten sposób
# def write_final_grade(subject_grades, final_grades = None):
#     if final_grades is None:
#         final_grades = []
#     grades_avg = sum(subject_grades) / len(subject_grades)
#     final_grades.append(int(grades_avg))
#     return final_grades

# tak jest ŹLE
# def write_final_grade(subject_grades, final_grades = []):
#     grades_avg = sum(subject_grades) / len(subject_grades)
#     final_grades.append(int(grades_avg))
#     return final_grades

# john_math_grades = [3, 4, 5, 2, 5]
# john_physics_grades = [4, 4, 4, 4]
# john_final_grades = write_final_grade(subject_grades=john_math_grades)
# john_final_grades = write_final_grade(subject_grades=john_physics_grades, final_grades=john_final_grades)
# print(f"Oceny John'a: {john_final_grades}")
#
# bob_math_grades = [5, 5, 5]
# bob_physics_grades = [3, 3, 3, 4, 4]
# bob_final_grades = write_final_grade(subject_grades=bob_math_grades)
# bob_final_grades = write_final_grade(subject_grades=bob_physics_grades, final_grades=bob_final_grades)
# print(f"Oceny Bob'a: {bob_final_grades}")
#
# # uwaga! Jeżeli jako domyślnego argumentu chcemy użyć Listy lub Słownika
# # należy to zrobić w ten sposób
# def do_something_with_default_dict(something = None):
#     if something is None:
#         something = {}
#     print("Tutja dalsza implementacja...")

# zadanie nr 1
# def change_number_range(number, tolerance_percentage=10):
#     tolerance_value = tolerance_percentage * number / 100
#     return [number - tolerance_value, number + tolerance_value]
#
# print(change_number_range(number=20))
# print(change_number_range(number=20, tolerance_percentage=50))

# zadanie nr 2
# def add_new_persons(names_str, subscribed_persons = None):
#     if subscribed_persons is None:
#         subscribed_persons = []
#     names = names_str.split(',')
#     for name in names:
#         subscribed_persons.append(name)
#     return subscribed_persons
#
# new_names = "Asia,Ania,Wojtek"
# new_course_participants = add_new_persons(new_names)
# print(new_course_participants)
# new_names = "Marcin,Ewa"
# new_course_participants = add_new_persons(new_names, subscribed_persons=new_course_participants)
# print(new_course_participants)

# rozwiązanie Mikołaja
# def add_people_to_classes(names_str, participants = None):
#     if participants is None:
#         participants = []
#     names = names_str.split(',')
#     # for name in names:
#     #     participants.append(name)
#     participants += names # dodawanie jednej listy do drugiej :)
#     return participants
#
# attendees_names = "Ola,Bob,Ala,Kuba"
# monday_course_participants = add_people_to_classes(attendees_names)
# print(monday_course_participants)
# attendees_names = "Paweł,Dorota"
# monday_course_participants = add_people_to_classes(attendees_names, participants=monday_course_participants)
# print(monday_course_participants)

# attendees_names = "Ania, Krzysztof"
# friday_course_participants = add_people_to_classes(attendees_names)
# print(friday_course_participants)

