import sys
import random

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsEllipseItem
from PyQt6.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Загрузка интерфейса из файла UI.ui
        loadUi("UI.ui", self)

        # Инициализация графической сцены
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        # Подключение обработчика нажатия кнопки
        self.pushButton.clicked.connect(self.draw_random_circles)

    def draw_random_circles(self):
        """Рисует случайные окружности желтого цвета."""
        # Очистка сцены перед рисованием новых окружностей
        self.scene.clear()

        # Генерация и отрисовка 5 случайных окружностей
        for _ in range(5):
            # Случайный диаметр окружности
            diameter = random.randint(20, 100)

            # Случайные координаты центра окружности
            x = random.randint(0, self.graphicsView.width() - diameter)
            y = random.randint(0, self.graphicsView.height() - diameter)

            # Создание окружности
            circle = QGraphicsEllipseItem(x, y, diameter, diameter)
            circle.setBrush(Qt.GlobalColor.yellow)  # Желтый цвет заливки

            # Добавление окружности на сцену
            self.scene.addItem(circle)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())