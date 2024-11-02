import random

import mysql.connector as mysql

db = mysql.Connect(
    user="st-onl",
    passwd="AVNS_tegPDkI5BlB2lW5eASC",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    database="st-onl"
)
cursor = db.cursor(dictionary=True)

# Создание студента
create_student = '''
INSERT INTO students (name, second_name)
VALUES (%s, %s);
'''
student = ('Uladzislau', 'Chabukin')
cursor.execute(create_student, student)
student_id = cursor.lastrowid

# Создание книг
create_book = '''
INSERT INTO books (title , taken_by_student_id)
VALUES (%s, %s);
'''
books = [
    ('1984', student_id),
    ('Скотный двор', student_id),
    ('Антиутопия', student_id)
]
book_ids = []
for book in books:
    cursor.execute(create_book, book)
    book_ids.append(cursor.lastrowid)

# Создание групп и добавление в нее студента
create_group = '''
INSERT INTO `groups` (title , start_date, end_date)
VALUES (%s, %s, %s);
'''
group = ('AutoQa', '01-11-2024', '01-12-2024')
cursor.execute(create_group, group)
group_id = cursor.lastrowid

set_student_in_group = '''
UPDATE students
SET group_id  = %s
WHERE id = %s;
'''
cursor.execute(set_student_in_group, (group_id, student_id))

# Создание учебных предметов
create_subjects = '''
INSERT INTO subjets (title)
VALUES (%s);
'''
subjects = [
    ('Chem',),
    ('Phys',),
    ('Math',)
]
subject_ids = []
for subject in subjects:
    cursor.execute(create_subjects, subject)
    subject_ids.append(cursor.lastrowid)

# Создание занятий для предметов
create_lesson = '''
INSERT INTO lessons (title, subject_id)
VALUES (%s, %s);
'''
lesson_ids = []
for subject_id in subject_ids:
    for i in range(2):
        cursor.execute(create_lesson, (f'ls_{i + 1}', subject_id))
        lesson_ids.append(cursor.lastrowid)

# Выставление отметок
put_marks = '''
INSERT INTO marks (value , lesson_id, student_id)
VALUES (%s, %s, %s);
'''
marks = ['Good', 'Not good', 'Bad', 'Not bad', 'SoSo']
for lesson_id in lesson_ids:
    cursor.execute(put_marks, (random.choice(marks), lesson_id, student_id))

# Получение отметок студентка
get_marks = '''
SELECT *
FROM marks
WHERE student_id = %s;'''
cursor.execute(get_marks, (student_id,))
student_marks = cursor.fetchall()
print(student_marks)

# Получить книги студента
get_books = '''
SELECT *
FROM books
WHERE taken_by_student_id = %s;'''
cursor.execute(get_books, (student_id,))
student_books = cursor.fetchall()
print(student_books)

# Получение всей информации о студенте
get_student_info = '''
SELECT s.name,
       s.second_name,
       g.title,
       b.title,
       m.value,
       l.title,
       s2.title
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id =l.id
JOIN subjets s2 ON l.subject_id = s2.id
WHERE s.id = %s;
'''
cursor.execute(get_student_info, (student_id,))
student_info = cursor.fetchall()
print(student_info)

db.commit()
db.close()
