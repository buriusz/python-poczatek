print("Hello world!")
# zmienne nazywamy małymi literami z podkreśleniami
# variable_valid_name = 5
# this_is_fine_2 = 20
# # STAŁE nazywamy wielkimi literami z podkreśleniami
# CONST_VALID_NAME = 3.14
#
# notValidName = 0
# NotValidName = 0
# NoTvALIdNaMe = 0

# W pythonie nie można rozpoczynać nazwy od cyfr
# 3_wont_work_at_all = 30

def run_average_speed_calculator(vehicle_name):
    distance = float(input(f"Podaj odległość jaką przebyłeś {vehicle_name} w km: "))
    time = float(input(f"Podaj czas w godzinach jaki zajęła Ci droga {vehicle_name}: "))
    avg_speed = distance / time
    print(f"Średnia prędkość jazdy {vehicle_name} wyniosła {avg_speed}km/h")

run_average_speed_calculator("rowerem")
run_average_speed_calculator("samochodem")
run_average_speed_calculator("pieszo")
