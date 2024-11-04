import csv
import os.path

import dotenv
import mysql.connector as mysql

dotenv.load_dotenv()

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)

db = mysql.Connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)
cursor = db.cursor(dictionary=True)

select_all_students = '''
SELECT s.name,
       s.second_name,
       g.title as group_title,
       b.title as book_title,
       s2.title as subject_title,
       l.title as lesson_title,
       m.value as mark_value
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id =l.id
JOIN subjets s2 ON l.subject_id = s2.id
'''
cursor.execute(select_all_students)
db_data = cursor.fetchall()

for student_data in data:
    if student_data not in db_data:
        print(student_data)
