class Car:
    """
    Класс, представляющий автомобиль.

    Attributes:
        make (str): Марка автомобиля.
        model (str): Модель автомобиля.
        mileage (int): Пробег автомобиля в километрах.
    """

    def __init__(self, make: str, model: str, mileage: int = 0):
        """
        Инициализация экземпляра класса Car.

        Args:
            make (str): Марка автомобиля.
            model (str): Модель автомобиля.
            mileage (int): Пробег автомобиля в километрах.

        >>> car = Car("Toyota", "Corolla", 50000)
        >>> car.make
        'Toyota'
        >>> car.model
        'Corolla'
        >>> car.mileage
        50000
        """
        self.make = make
        self.model = model
        self.mileage = mileage

    def drive(self, distance: int) -> None:
        """
        Увеличивает пробег автомобиля на указанное расстояние.

        Args:
            distance (int): Расстояние в километрах.

        >>> car = Car("Toyota", "Corolla", 50000)
        >>> car.drive(100)
        >>> car.mileage
        50100
        """
        if distance < 0:
            raise ValueError("Расстояние не может быть отрицательным")
        self.mileage += distance

    def get_info(self) -> str:
        """
        Возвращает информацию об автомобиле.

        Returns:
            str: Информация об автомобиле.

        >>> car = Car("Toyota", "Corolla", 50000)
        >>> car.get_info()
        'Toyota Corolla, пробег: 50000 км'
        """
        return f"{self.make} {self.model}, пробег: {self.mileage} км"


class Book:
    """
    Класс, представляющий книгу.

    Attributes:
        title (str): Название книги.
        author (str): Автор книги.
        pages (int): Количество страниц.
    """

    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация экземпляра класса Book.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            pages (int): Количество страниц.

        >>> book = Book("1984", "George Orwell", 328)
        >>> book.title
        '1984'
        >>> book.author
        'George Orwell'
        >>> book.pages
        328
        """
        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages_read: int) -> str:
        """
        Симулирует чтение книги и возвращает сообщение о прогрессе.

        Args:
            pages_read (int): Количество прочитанных страниц.

        Returns:
            str: Сообщение о прогрессе чтения.

        >>> book = Book("1984", "George Orwell", 328)
        >>> book.read(50)
        'Вы прочитали 50 страниц. Осталось 278 страниц.'
        """
        if pages_read < 0:
            raise ValueError("Количество прочитанных страниц не может быть отрицательным")
        if pages_read > self.pages:
            raise ValueError("Вы не можете прочитать больше страниц, чем есть в книге")
        self.pages -= pages_read
        return f"Вы прочитали {pages_read} страниц. Осталось {self.pages} страниц."

    def get_info(self) -> str:
        """
        Возвращает информацию о книге.

        Returns:
            str: Информация о книге.

        >>> book = Book("1984", "George Orwell", 328)
        >>> book.get_info()
        '1984, автор: George Orwell, страниц: 328'
        """
        return f"{self.title}, автор: {self.author}, страниц: {self.pages}"


class Student:
    """
    Класс, представляющий студента.

    Attributes:
        name (str): Имя студента.
        age (int): Возраст студента.
        grades (list[int]): Список оценок студента.
    """

    def __init__(self, name: str, age: int):
        """
        Инициализация экземпляра класса Student.

        Args:
            name (str): Имя студента.
            age (int): Возраст студента.

        >>> student = Student("Алексей", 20)
        >>> student.name
        'Алексей'
        >>> student.age
        20
        >>> student.grades
        []
        """
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade: int) -> None:
        """
        Добавляет оценку в список оценок студента.

        Args:
            grade (int): Оценка студента.

        >>> student = Student("Алексей", 20)
        >>> student.add_grade(5)
        >>> student.grades
        [5]
        """
        if grade < 1 or grade > 5:
            raise ValueError("Оценка должна быть от 1 до 5")
        self.grades.append(grade)

    def average_grade(self) -> float:
        """
        Вычисляет средний балл студента.

        Returns:
            float: Средний балл.

        >>> student = Student("Алексей", 20)
        >>> student.add_grade(5)
        >>> student.add_grade(4)
        >>> student.average_grade()
        4.5
        """
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_info(self) -> str:
        """
        Возвращает информацию о студенте.

        Returns:
            str: Информация о студенте.

        >>> student = Student("Алексей", 20)
        >>> student.add_grade(5)
        >>> student.add_grade(4)
        >>> student.get_info()
        'Студент: Алексей, возраст: 20, средний балл: 4.5'
        """
        return f"Студент: {self.name}, возраст: {self.age}, средний балл: {self.average_grade()}"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
