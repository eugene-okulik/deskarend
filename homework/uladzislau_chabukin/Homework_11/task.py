class Book:
    material = "бумага"
    has_text = True

    def __init__(self, title, author, page_count, isbn, reserved=False):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.reserved = reserved

    def reserve(self):
        self.reserved = True

    def get_info(self):
        return (f"Название: {self.title}, Автор: {self.author}, страниц: {self.page_count}, "
                f"материал: {self.material}{', зарезервирована' if self.reserved else ''} ")


class SchoolBook(Book):
    def __init__(self, title, author, page_count, subject, school_lvl, isbn, has_tasks=True, reserved=False):
        super().__init__(title, author, page_count, isbn)
        self.subject = subject
        self.school_lvl = school_lvl
        self.has_tasks = has_tasks
        self.reserved = reserved

    def get_textbook_info(self):
        return (f"Название: {self.title}, Автор: {self.author}, страниц: {self.page_count}, "
                f"предмет: {self.subject}, класс: {self.school_lvl}{', зарезервирована' if self.reserved else ''} ")


book_1 = Book('Идиот', 'Достоевский', 500, 'cool_book_1')
book_2 = Book('1984', 'Джордж Оруэлл', 233.4, 'cool_book_2')
book_3 = Book('Скотный двор', 'Джордж Оруэлл', 150, 'cool_book_3')
book_4 = Book('Противостояние', 'Противостояние', 700, 'cool_book_4')
book_5 = Book('Старик и море', 'Эрнест Хемингуэй', 444, 'cool_book_5')

book_5.reserve()

for book in (book_1, book_2, book_3, book_4, book_5):
    print(book.get_info())
print()

math = SchoolBook('Алгебра', 'Иванов', 200, 'Математика', 3, 'math1234')
chemistry = SchoolBook('Полимеры', 'Петров', 999, 'Химия', 7, 'chem1234')
physics = SchoolBook('Оптика', 'Сидоров', 467, 'Физика', 5, 'phys1234')

chemistry.reserve()

for textbook in (math, chemistry, physics):
    print(textbook.get_textbook_info())
