import json
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class Weather:
    def __init__(self, city, temperature, unit):
        self.city, self.temperature, self.unit = city, temperature, unit

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def create_objects(data):
    return [Weather(item['city'], item['temperature'], item['unit']) for item in data]

def display_data(weather_objects):
    app = QApplication([])
    window = QWidget()
    table = QTableWidget()
    table.setRowCount(len(weather_objects))
    table.setColumnCount(3)
    table.setHorizontalHeaderLabels(['Город', 'Температура', 'Ед измерения'])

    for row, weather in enumerate(weather_objects):
        table.setItem(row, 0, QTableWidgetItem(weather.city))
        table.setItem(row, 1, QTableWidgetItem(str(weather.temperature)))
        table.setItem(row, 2, QTableWidgetItem(weather.unit))

    layout = QVBoxLayout()
    layout.addWidget(table)
    window.setLayout(layout)
    window.show()
    app.exec_()

file_path = 'gyabraa.json'
data = load_data(file_path)
weather_objects = create_objects(data)
display_data(weather_objects)