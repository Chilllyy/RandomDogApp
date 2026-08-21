import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QColorDialog, QStyleFactory
from PySide6.QtCore import QByteArray, Qt
from PySide6.QtGui import QPixmap, QPalette, QColor
import requests
from src.test.main_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.nextButton.clicked.connect(self.next)

        url = "https://dog.ceo/api/breeds/list/all"
        response = requests.get(url)
        self.data = response.json()
        sub_breeds = []
        breed_list = list(self.data['message'].keys())
        self.dogBreedList.addItems(breed_list)
        self.randomBreedButton.clicked.connect(self.random)

        self.guiColorButton.clicked.connect(self.gui_color)
        self.buttonColorButton.clicked.connect(self.button_color)
        self.dogBreedList.currentIndexChanged.connect(self.update_sub_breeds)

        self.next()

    def next(self):
        dog_breed = self.dogBreedList.currentText()
        dog_sub_breed = self.dogSubBreedList.currentText()
        if dog_breed == "All":
            url = f"https://dog.ceo/api/breeds/image/random"
        else:
            if dog_sub_breed == "All":
                url = f"https://dog.ceo/api/breed/{dog_breed}/images/random"
            else:
                url = f"https://dog.ceo/api/breed/{dog_breed}/{dog_sub_breed}/images/random"
        response = requests.get(url)
        data = response.json()
        message = data.get('message')
        self.get_image(message)

    def button_color(self):
        palette = self.nextButton.palette()
        initial = palette.color(self.nextButton.backgroundRole())
        color = QColorDialog().getColor(initial=initial)
        if not color.isValid(): return
        palette.setColor(self.nextButton.backgroundRole(), color)
        self.nextButton.setPalette(palette)

    def gui_color(self):
        palette = self.palette()
        initial = palette.color(self.backgroundRole())
        color = QColorDialog().getColor(initial=initial)
        if not color.isValid(): return
        palette.setColor(self.backgroundRole(), color)
        self.setPalette(palette)

    def random(self):
        total = self.dogBreedList.count()
        if total > 0:
            random_index = random.randint(0, total - 1)
            self.dogBreedList.setCurrentIndex(random_index)
            self.update_sub_breeds()
            self.random_sub()

    def random_sub(self):
        total = self.dogSubBreedList.count()
        if total > 1:
            index = random.randint(1, total - 1)
            self.dogSubBreedList.setCurrentIndex(index)


    def get_image(self, url):
        image_req = requests.get(url)
        image_data = image_req.content

        qbyte_array = QByteArray(image_data)
        pixmap = QPixmap()
        success = pixmap.loadFromData(qbyte_array)

        if success:
            self.dogImage.setPixmap(pixmap.scaled(800, 800, aspectMode=Qt.AspectRatioMode.KeepAspectRatio, mode=Qt.TransformationMode.SmoothTransformation))
        else:
            print("Unable to load Image")

    def update_sub_breeds(self):
        self.dogSubBreedList.clear()
        self.dogSubBreedList.addItem("All")
        breed = self.dogBreedList.currentText()
        if self.data['message'][breed]:
            self.dogSubBreedList.addItems(self.data['message'][breed])

def main():
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()