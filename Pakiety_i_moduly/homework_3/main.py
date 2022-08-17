import calculations.investment

def ask_for_float_value(message):
    input_value = input(message)
    return float(input_value)

print("Kalkulator wartości lokaty z roczną kapitalizacją.")

initial_value = ask_for_float_value("Jaką kwotę wpłaciłeś(zł)? ")
percentage = ask_for_float_value("Jakie jest oprocentowanie(%)? ")
years = ask_for_float_value("Ile lat trwa lokata? ")
final_value = calculations.investment.calculate_investment_value(initial_value=initial_value, percentage=percentage, years=years)
print(f"Po {int(years)} latach Twoja lokata będzie wynosić {final_value:.2f}zł")