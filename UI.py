class UI:
    def __init__(self, screen):
        """
        :param screen - экран, нужно для отрисовки объектов
        """

        self.screen =  screen
        self.UI_elements = []

    def add_button(self, sscreen, color: tuple, pos, width: int, height: int) -> None:
        """
        Добавляет экземпляр класса "Кнопка" в массив всех элементов

        :param screen, color, pos, width, height - требуются для создания экземпляра
        класса Button
        """
        pass

    def add_text(self, screen, color, pos, size: int, phrase: str) -> None:
        """
        Добавляет экземпляр класса "Текст" в массив всех элементов

        :param screen, color, pos, size, phrase - требуются для создания экземпляра
        класса Text
        """
        pass

    def update(self, events) -> None:
        """
        Функция обрабатывает все события, нужно для вызва функции on_click()

        :param events - массив со всеми событиями, нужно для обработки нажатий
        """
        pass

    def draw(self) -> None:
        """
        Функция вызывает функцию draw() у всез элементов из массива UI_elements
        """
        pass


if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
