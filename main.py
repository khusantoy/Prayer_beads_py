from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)

class Prayer_beads(QWidget):
    def __init__(self) -> None:
        super().__init__()



        self.show()

app = QApplication([])
win = Prayer_beads()
app.exec_()