import os

def task1():
    def translateLetter(*letters):
        grade_points = {'A+': 4.3, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
                        'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'D-': 0.7}

        return [grade_points.get(letter, 0.0) for letter in letters]

    def translatePercentage(*percentages):
        grade_points = {range(95, 101): 4.3, range(90, 95): 4.0, range(85, 90): 3.7,
                        range(80, 85): 3.3, range(75, 80): 3.0, range(70, 75): 2.7,
                        range(65, 70): 2.3, range(60, 65): 2.0, range(55, 60): 1.7,
                        range(50, 55): 1.3, range(45, 50): 1.0, range(40, 45): 0.7}

        return [next((grade_points[range_grade] for range_grade in grade_points if percentage in range_grade), 0.0) for
                percentage in percentages]

    def calculateGPA(*args):
        if len(args) % 2 != 0:
            return ValueError("Error")

        total_points = sum(args[i] * args[i + 1] for i in range(0, len(args), 2))
        total_credits = sum(args[i + 1] for i in range(0, len(args), 2))

        return total_points / total_credits if total_credits != 0 else 0.0

    def process_course_file(course_filename):
        with open(course_filename, 'r') as file:
            grades = [line.strip().split()[1] for line in file.readlines() if len(line.strip().split()) >= 2]

        grade_points = translateLetter(*grades)  # Используем translateLetter для примера
        return calculateGPA(*grade_points)

    # Чтение баллов из файла credits.txt
    with open('grades/credits.txt', 'r') as credits_file:
        credit_points = [float(line.strip().split()[1]) for line in credits_file.readlines()]

    # Общий средний балл
    overall_average = calculateGPA(*credit_points)

    # Обработка каждого курса и сохранение результатов в overallGPAs.txt
    with open('grades/overallGPAs.txt', 'w') as overall_file:
        overall_file.write(f'Overall GPA: {overall_average}\n\n')

        courses = ['math', 'chemistry', 'english']
        for course in courses:
            course_filename = f'grades/{course}.txt'
            course_average = process_course_file(course_filename)

            overall_file.write(f'{course.capitalize()} GPA: {course_average}\n')

    translateLetter("A+")
    translatePercentage(75)
    calculateGPA(3.3, 4, 2.7, 3, 4.0, 4)

if __name__ == "__main__":
    task1()



# API:
# Определение: API (интерфейс прикладного программирования) представляет собой набор правил, позволяющих различным программам взаимодействовать друг с другом.
# Применение: API используется для интеграции, автоматизации, помощи в разработке и контроля доступа.
# Пример с Python: С помощью библиотеки requests можно взаимодействовать с API, например, получать данные по URL.
# Ограничения: У API могут быть ограничения на количество запросов, уязвимости безопасности, риски зависимости и ограничения доступа к данным.
# Socket:
# Определение: Сокет представляет собой конечную точку, обеспечивающую связь между двумя узлами по сети.
# Применение: Сокеты используются для обмена данными между клиентом и сервером, а также для реального времени в приложениях.
# Пример на Python: Создание базового сервера и клиента с помощью библиотеки socket для обмена данными.