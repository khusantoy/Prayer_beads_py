from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)

class Prayer_beads(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(300, 300)
        self.setWindowTitle("Tasbex")
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.count = 0
        self.index = 0
        self.zikrlar = ("Subhanalloh", "Alhamdulillah", "Allohu Akbar")
        self.on = False

        self.zikr_label = QLabel(self.zikrlar[0])
        self.count_edit = QLineEdit(f'{self.count}')
        self.count_btn = QPushButton('+')
        self.reset_btn = QPushButton("Reset")
        self.power_btn = QPushButton("Power")

        self.h_box.addWidget(self.reset_btn)
        self.h_box.addStretch()
        self.h_box.addWidget(self.power_btn)

        self.v_box.addWidget(self.zikr_label)
        self.v_box.addWidget(self.count_edit)
        self.v_box.addLayout(self.h_box)
        self.v_box.addWidget(self.count_btn)

        self.setLayout(self.v_box)

        self.count_btn.clicked.connect(self.on_press)

        self.show()

    def on_press(self):
        self.count += 1
        if self.count == 34:
            self.index += 1
            self.zikr_label.setText(self.zikrlar[self.index % 3])
            self.count = 0
        self.count_edit.setText(f'{self.count}')

    def off_on(self):
        self.on = not self.on

        if self.on:
            pass

app = QApplication([])
win = Prayer_beads()
app.exec_()