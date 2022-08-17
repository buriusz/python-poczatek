import math
def triangle_hypotenuse_calculator(base, altitude):
    return math.sqrt(math.pow(base, 2) + math.pow(altitude, 2))

base = float(input("Podaj długość trójkąta: "))
altitude = float(input("Podaj wysokość trójkąta: "))
triangle_hypotenuse = triangle_hypotenuse_calculator(base= base, altitude=altitude)
print(f"Długość przeciwprostokątnej trójkąta prostokątnego wynosi: {triangle_hypotenuse}")