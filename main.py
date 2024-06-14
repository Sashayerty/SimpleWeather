import io
import json
import sys
from PyQt5 import uic
from data.get_weather import get_weather as get
from data.simple_weather_action import simple_weather_action as hi
from templates.weather import weather
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

class SimpleWeatherWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.set_ui()
        self.functions()
    
    def set_ui(self):
        ui = io.StringIO(weather)
        uic.loadUi(ui, self)

    def functions(self):
        with open("place.json", "r") as data:
            self.place_in_file = json.load(data)
            if self.place_in_file["place"] == '':
                self.place.setPlaceholderText('Введите место')
            else:
                self.place.setPlaceholderText(self.place_in_file["place"])
                self.data = get('+'.join(self.place_in_file["place"].split()))
                self.Weather.setText(self.data[:].replace('Follow @igor_chubin for wttr.in updates', ''))

        self.btn_change_place.clicked.connect(self.change_place)
        self.btn_update.clicked.connect(self.updater)

    def change_place(self):
        self.place_data = self.place.text()
        if self.place_data == '':
            self.place.setPlaceholderText('Введите место')
        else:
            self.place.setText('')
            self.place.setPlaceholderText(self.place_data) if self.place_data else self.place.setPlaceholderText('Введите место')
            self.data = get('+'.join(self.place_data.split()))
            self.Weather.setText(self.data[:].replace('Follow @igor_chubin for wttr.in updates', ''))
            self.data = {"place":self.place_data}
            with open('place.json', 'w', encoding="utf-8") as file:
                json.dump(self.data, file, ensure_ascii=False, indent=4)

    def updater(self):
        with open("place.json", "r") as data:
            self.place_in_file = json.load(data)
            if not self.place_in_file["place"]:
                self.place.setPlaceholderText('Введите место')
            else:
                self.data = get('+'.join(self.place_in_file["place"].split()))
                self.place.setPlaceholderText(self.place_in_file["place"])
                self.Weather.setText(self.data[:].replace('Follow @igor_chubin for wttr.in updates', ''))

if __name__ == '__main__':
    hi()
    app = QApplication(sys.argv)
    ex = SimpleWeatherWindow()
    ex.show()
    sys.exit(app.exec_())
