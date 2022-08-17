import speed_calculator

running_distance = float(input(f"Podaj odległość jaką przebiegłeś w km: "))
running_time = float(input(f"Podaj czas w godzinach jaki zajęła Ci droga: "))
avg_speed = speed_calculator.avg_speed(distance=running_distance, time=running_time)
print(f"Średnia prędkość biegu wyniosła {avg_speed:.2f}km/h")
