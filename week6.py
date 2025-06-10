import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QSlider, QGroupBox, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor

class FontAdjuster(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Font & Color Adjuster - Week 6")
        self.setGeometry(100, 100, 500, 400)
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout()

        # Label utama (NIM)
        self.label = QLabel("F1D021099", self)
        self.label.setFont(QFont("Arial", 30))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")

        # Nama di bawah
        self.nameLabel = QLabel("Lalu Avryan Adjie Pratama")
        self.nameLabel.setAlignment(Qt.AlignCenter)
        self.nameLabel.setStyleSheet("font-size: 14px;")

        # Font size slider
        self.fontSlider = self.createSlider(20, 60, self.changeFontSize, "Font Size")

        # Font color slider (grayscale)
        self.fontColorSlider = self.createSlider(0, 255, self.changeFontColor, "Font Color (Grayscale)")

        # Background color slider (grayscale)
        self.bgColorSlider = self.createSlider(0, 255, self.changeBackgroundColor, "Background Color (Grayscale)")

        layout.addWidget(self.label)
        layout.addWidget(self.nameLabel)
        layout.addWidget(self.fontSlider["group"])
        layout.addWidget(self.fontColorSlider["group"])
        layout.addWidget(self.bgColorSlider["group"])

        self.setLayout(layout)

    def createSlider(self, minVal, maxVal, onChange, title):
        group = QGroupBox(title)
        groupLayout = QVBoxLayout()
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(minVal)
        slider.setMaximum(maxVal)
        slider.setValue((minVal + maxVal) // 2)
        slider.valueChanged.connect(onChange)
        groupLayout.addWidget(slider)
        group.setLayout(groupLayout)
        return {"slider": slider, "group": group}

    def changeFontSize(self):
        size = self.fontSlider["slider"].value()
        font = self.label.font()
        font.setPointSize(size)
        self.label.setFont(font)

    def changeFontColor(self):
        value = self.fontColorSlider["slider"].value()
        self.updateLabelStyle(text_color=value, bg_color=None)

    def changeBackgroundColor(self):
        value = self.bgColorSlider["slider"].value()
        self.updateLabelStyle(text_color=None, bg_color=value)

    def updateLabelStyle(self, text_color=None, bg_color=None):
        # Ambil nilai sekarang
        current_style = self.label.styleSheet()
        color_vals = {
            "text": self.fontColorSlider["slider"].value(),
            "bg": self.bgColorSlider["slider"].value()
        }
        # Jika hanya satu yang berubah
        if text_color is not None:
            color_vals["text"] = text_color
        if bg_color is not None:
            color_vals["bg"] = bg_color

        new_style = f"color: rgb({color_vals['text']},{color_vals['text']},{color_vals['text']});" \
                    f" background-color: rgb({color_vals['bg']},{color_vals['bg']},{color_vals['bg']});"
        self.label.setStyleSheet(new_style)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FontAdjuster()
    window.show()
    sys.exit(app.exec_())
