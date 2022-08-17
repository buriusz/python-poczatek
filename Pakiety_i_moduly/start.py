print(__name__)
# from .school import promotion_status # relative import nie działa
# from .school.grade_calculator import calculate_student_final_grades # relative import nie działa
# from .school.promote import check_promotion # relative import nie działa
# from .school.students_data import is_student_in_school # relative import nie działa

from school import promotion_status
from school.grade_calculator import calculate_student_final_grades
from school.promote import check_promotion
from school.students_data import is_student_in_school

print("WItaj w elektronicznym dzienniku!")

student_name = input("Podaj imię ucznia, żeby dowiedzieć się czy zdał/a: ")

if not is_student_in_school(student_name):
    print(f"Niestety {student_name} nie ma na liście :(")
else:
    final_grades = calculate_student_final_grades(student_name)
    promotion_result = check_promotion(final_grades)

    if promotion_result == promotion_status.PASSED:
        print(f"Gratuluję! {student_name} zdał/a :)")
    elif promotion_result == promotion_status.FAILED:
        print(f"Niestety. {student_name} nie zdał/a :(")
    else:
        print("Coś poszło nie tak... :( Zgłoś to obsłudze systemu.")