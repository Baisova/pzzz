import json
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QComboBox, QLabel

class Weather:
    def __init__(self, city, temperature, unit):
        self.city, self.temperature, self.unit = city, temperature, unit

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def create_objects(data):
    return [Weather(item['city'], item['temperature'], item['unit']) for item in data]

class WeatherApp(QWidget):
    def __init__(self, weather_objects):
        super().__init__()
        self.weather_objects = weather_objects
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Данные о погоде')
        layout = QVBoxLayout()

        self.combo_box = QComboBox()
        self.combo_box.addItems(['Все', 'Минимальная температура', 'Максимальная температура', 'Средняя температура'])
        self.combo_box.currentTextChanged.connect(self.update_table)

        layout.addWidget(QLabel('Выбор температуры:'))
        layout.addWidget(self.combo_box)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Город', 'Температура', 'Eд.измерения'])
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.update_table('Все')

    def update_table(self, selection):
        if selection == 'Минимальная температура':
            min_temp = min(w.temperature for w in self.weather_objects)
            data = [w for w in self.weather_objects if w.temperature == min_temp]
        elif selection == 'Максимальная температура':
            max_temp = max(w.temperature for w in self.weather_objects)
            data = [w for w in self.weather_objects if w.temperature == max_temp]
        elif selection == 'Средняя температура':
            avg_temp = sum(w.temperature for w in self.weather_objects) / len(self.weather_objects)
            data = [Weather('Средняя', round(avg_temp, 2), 'C')] 
        else:
            data = self.weather_objects

        self.table.setRowCount(len(data))
        for row, weather in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(weather.city))
            self.table.setItem(row, 1, QTableWidgetItem(str(weather.temperature)))
            self.table.setItem(row, 2, QTableWidgetItem(weather.unit))

file_path = 'gyabraa.json'
data = load_data(file_path)
weather_objects = create_objects(data)

app = QApplication([])
window = WeatherApp(weather_objects)
window.show()
app.exec_()