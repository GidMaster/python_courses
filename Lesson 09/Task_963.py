"""
Deanery
"""

def do_filter(students_list, key_word, value):
    """
    filtring list of students by one of keys
    """
    return [student for student in students_list if student[key_word] == value]
     

def do_sort(students_list, key_word):
    """
    Sorting list of students by one of keys
    """
    return sorted(students_list, key=lambda student: student[key_word])

def get_uniq_values(students_list, key_word):
    """
    Return list of uniq values from sltudent list by one of keys
    """
    return set(student[key_word] for student in students_list)

def get_avg_degrees(students_list):
    """
    Return dictionary of averange degrees for each group for each course (math, art etc)
    """
    #get amount of groups
    amount_of_groups = get_uniq_values(students_list, 'group')
    result = {}
    # for each group calculating averange degrees for each course
    for group in amount_of_groups:
        students_in_group = do_filter(students_list, 'group', group)
        number_of_students_in_group = len(students_in_group)
        avg_degree_math = sum(student['math'] for student in students_in_group) / number_of_students_in_group
        avg_degree_physic = sum(student['physic'] for student in students_in_group) / number_of_students_in_group
        avg_degree_art = sum(student['art'] for student in students_in_group) / number_of_students_in_group
        avg_degree_programming = sum(student['programming'] for student in students_in_group) / number_of_students_in_group
        avg_degree_networking = sum(student['networking'] for student in students_in_group) / number_of_students_in_group
        result[group] = {'math': avg_degree_math, 'physic': avg_degree_physic, 'art': avg_degree_art, 'programming': avg_degree_programming,'networking': avg_degree_networking}
    return result

def get_best_student_of_group(students_list):
    """
    Return dictionary which contains students from each group with best degrees
    """
    amount_of_groups = get_uniq_values(students_list, 'group')
    number_of_courses = 5
    result = {}
    for group in amount_of_groups:
        students_in_group = do_filter(students_list, 'group', group)
        best_student = max(students_in_group, key=lambda student: (student['math'] + student['physic'] + student['art'] + student['programming'] + student['networking']) / number_of_courses)
        result[group] = best_student
    return result

def get_students_age(students_list):
    """
    return entries of older and younger students
    """
    #sorting students by birthday
    students_sorted_by_age = do_sort(students_list, 'birthday')
    return students_sorted_by_age[0], students_sorted_by_age[-1]

def get_students_by_course(students_list):
    #get amount of courses
    amount_of_courses = get_uniq_values(students_list, 'course')
    #get students entry by course and sorting them by name
    result = []
    for course in amount_of_courses:
        result += (do_sort(do_filter(students_list, 'course', course), 'surname'))
    return result
        


def main():
    students = [
        {'surname': 'Ivanov', 'name': 'Ivan', 'second_name': 'Ivanovich', 'birthday': 1987, 'course': 5, 'group': 145, 'math': 5, 'physic': 4, 'art': 3, 'programming': 5, 'networking': 4},
        {'surname': 'Ivanova', 'name': 'Maria', 'second_name': 'Ivanovna', 'birthday': 1989, 'course': 4, 'group': 146, 'math': 4, 'physic': 4, 'art': 3, 'programming': 4, 'networking': 4},
        {'surname': 'Petrov', 'name': 'Peter', 'second_name': 'Petrovich', 'birthday': 1988, 'course': 5, 'group': 145, 'math': 3, 'physic': 5, 'art': 3, 'programming': 3, 'networking': 5},
        {'surname': 'Arkhipov', 'name': 'Vasiliy', 'second_name': 'Sergeevich', 'birthday': 1986, 'course': 5, 'group': 165, 'math': 4, 'physic': 4, 'art': 5, 'programming': 5, 'networking': 4},
        {'surname': 'Bobrova', 'name': 'Tatiana', 'second_name': 'Vasilievna', 'birthday': 1989, 'course': 5, 'group': 165, 'math': 5, 'physic': 4, 'art': 5, 'programming': 5, 'networking': 5},
        {'surname': 'Losev', 'name': 'Sergey', 'second_name': 'Trofimovich', 'birthday': 1989, 'course': 4, 'group': 146, 'math': 3, 'physic': 5, 'art': 5, 'programming': 5, 'networking': 3},
        {'surname': 'Slonova', 'name': 'Yana', 'second_name': 'Alekseevna', 'birthday': 1989, 'course': 4, 'group': 156, 'math': 4, 'physic': 4, 'art': 5, 'programming': 3, 'networking': 3},
        {'surname': 'Solovev', 'name': 'Artem', 'second_name': 'Dmitrievich', 'birthday': 1988, 'course': 5, 'group': 165, 'math': 5, 'physic': 5, 'art': 3, 'programming': 3, 'networking': 4},
        {'surname': 'Alekseev', 'name': 'Vitaliy', 'second_name': 'Borisovich', 'birthday': 1991, 'course': 5, 'group': 145, 'math': 5, 'physic': 5, 'art': 5, 'programming': 5, 'networking': 5}
    ]

    grouped_by_course = get_students_by_course(students)
    print('----------------------------------------------------------------------------')
    print('Students\' list groupped by course:')
    print('----------------------------------------------------------------------------')
    for student in grouped_by_course:
        print(f'{student["surname"]} {student["name"]} course {student["course"]}')
    print('----------------------------------------------------------------------------')
    print('----------------------------------------------------------------------------')
    avg_degrees = get_avg_degrees(students)
    print('----------------------------------------------------------------------------')
    print('Averenge degrees for each group.')
    print('----------------------------------------------------------------------------')
    for group in avg_degrees:
        print(f'Group: {group}')
        for course in avg_degrees[group]:
            print(f'--{course}: {round(avg_degrees[group][course], 2)}')
    print('----------------------------------------------------------------------------')
    print('----------------------------------------------------------------------------')
    older_student , younger_student = get_students_age(students)
    print('----------------------------------------------------------------------------')
    print(f'Older student is {older_student["surname"]} {older_student["name"]}. Was born in {older_student["birthday"]}')
    print(f'Younger student is {younger_student["surname"]} {younger_student["name"]}. Was born in {younger_student["birthday"]}')
    print('----------------------------------------------------------------------------')
    print('----------------------------------------------------------------------------')
    best_students = get_best_student_of_group(students)
    print('----------------------------------------------------------------------------')
    print('List of best students')
    print('----------------------------------------------------------------------------')
    for group in best_students:
        print(f'Group: {group}. {best_students[group]["surname"]} {best_students[group]["name"]}')
    print('----------------------------------------------------------------------------')
    print('----------------------------------------------------------------------------')

if __name__ == '__main__':
    main()
