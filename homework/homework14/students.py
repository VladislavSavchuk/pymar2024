"""Students.
This program writes the list of students, group number,
and their grades to a file. It opens the file and displays the total
number of students, the number of students for each group,
and the average grade for each group.
"""

import itertools


def write_data_in_file(students_data: list):
    """Writes student data to a file"""
    with open('students.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(students_data) + '\n')


def read_data_in_file() -> list:
    """Reads student data from a file and returns a list of students."""

    students = []

    with open('students.txt', 'r', encoding='utf-8') as file:
        for line in file:
            content = line.split(',')
            name = content[0]
            group = content[1]
            grades = list(map(int, content[2:]))
            students.append((name, group, grades))
    return students


def data_record_processing(students: list) -> tuple:
    """Calculates statistics for groups of students."""

    total_students = len(students)

    students.sort(key=lambda content: content[1])

    group_stats = {}

    for group, group_students in \
            (itertools.groupby(students, key=lambda content: content[1])):
        list_students = list(group_students)
        count = len(list_students)
        total_grades = sum(len(student[2]) for student in list_students)
        sum_grades = sum(sum(student[2]) for student in list_students)

        if total_grades > 0:
            average_grade = sum_grades / total_grades
        else:
            average_grade = 0
        group_stats[group] = {'count': count,
                              'average_grade': average_grade}
    return total_students, group_stats


def additional_data_to_file(total_students: int, group_stats: dict):
    """Adds statistics to the end of the file."""
    with open('students.txt', 'a', encoding='utf-8') as file:
        file.write(f'\nTotal students: {total_students}\n')
        for group, data in group_stats.items():
            file.write(f"Group {group}: {data['count']} students, "
                       f"Average_grade: {round(data['average_grade'], 2)}\n")
    print('Data has been adds')


def main():
    """Start the program"""
    students_data = [
        "Serena Williams,1A,5,4,4,3",
        "Lionel Messi,2B,4,3,5,2",
        "Kobe Bryant,1A,3,5,4,1",
        "LeBron James,3C,5,5,4,5",
        "Jason Brown,2B,4,3,4,4",
        "Cristiano Ronaldo,3C,5,5,5,4",
        "Alisa Schmidt,1A,4,4,4,5",
        "Marko Reus,2B,3,3,4,5",
        "Erling Holland,3C,5,4,5,5",
        "Roberto Carlos,1A,1,1,0,1"
    ]

    try:
        write_data_in_file(students_data)
        students = read_data_in_file()
        total_students, group_data = data_record_processing(students)
        additional_data_to_file(total_students, group_data)
    except FileNotFoundError:
        print("File not found")
    except (IOError, ValueError) as e:
        print(e)


main()
