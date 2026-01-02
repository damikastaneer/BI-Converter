from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from converter.number_converter import NumberConverter


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/main_window.ui", self)

        # Base mapping
        self.base_map = {"Binair": 2, "Decimaal": 10, "Hexadecimaal": 16}

        self.convertButton.clicked.connect(self.convert)

    def convert(self):
        value = self.inputLineEdit.text()
        input_base = self.base_map[self.inputBaseCombo.currentText()]
        output_base = self.base_map[self.outputBaseCombo.currentText()]

        try:
            converter = NumberConverter(value, input_base)
            result = converter.convert_to(output_base)

            self.resultLabel.setText(result)
            self.errorLabel.setText("")

        except ValueError:
            self.errorLabel.setText("Ongeldige invoer")
            self.resultLabel.setText("")
