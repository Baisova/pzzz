import json
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QSpinBox, QLabel

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
        self.filtered_objects = weather_objects.copy()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, 100) 
        self.spin_box.valueChanged.connect(self.filter_data) 

        layout.addWidget(QLabel('Фильтер температуры:'))
        layout.addWidget(self.spin_box)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Город', 'Температура', 'Ед.измерения'])
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.update_table(self.weather_objects)

    def update_table(self, data):
        self.table.setRowCount(len(data))
        for row, weather in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(weather.city))
            self.table.setItem(row, 1, QTableWidgetItem(str(weather.temperature)))
            self.table.setItem(row, 2, QTableWidgetItem(weather.unit))

    def filter_data(self):
        filter_value = self.spin_box.value()
        if filter_value == 0:
            self.filtered_objects = self.weather_objects.copy()
        else:

            self.filtered_objects = [w for w in self.weather_objects if w.temperature >= filter_value]
        self.update_table(self.filtered_objects)

file_path = 'gyabraa.json'
data = load_data(file_path)
weather_objects = create_objects(data)

app = QApplication([])
window = WeatherApp(weather_objects)
window.show()
app.exec_()