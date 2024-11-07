from PyQt5.QtWidgets import QDialog,QLineEdit,QVBoxLayout,QPushButton,QLabel


class AnnealingPopup(QDialog):
    def __init__(self, parent = None, val1 = 1000, val2 = 0.995, val3 = 1000, name1 = "начальная температура", name2 = "коэффициент охлаждения", name3 = "кол-во итераций"):
        super(AnnealingPopup, self).__init__()
        self.name1 = QLabel(self)
        self.name1.setText(name1)
        self.name2 = QLabel(self)
        self.name2.setText(name2)
        self.name3 = QLabel(self)
        self.name3.setText(name3)
        self.val1 = QLineEdit(self)
        self.val1.setFixedWidth(40)
        self.val1.setText(str(val1))
        self.val2 = QLineEdit(self)
        self.val2.setFixedWidth(40)
        self.val2.setText(str(val2))
        self.val3 = QLineEdit(self)
        self.val3.setFixedWidth(40)
        self.val3.setText(str(val3))
        layout = QVBoxLayout()
        self.ok_btn = QPushButton("Ok", self)
        self.cancel_btn = QPushButton("Cancel", self)
        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)
        layout.addWidget(self.name1)
        layout.addWidget(self.val1)
        layout.addWidget(self.name2)
        layout.addWidget(self.val2)
        layout.addWidget(self.name3)
        layout.addWidget(self.val3)
        layout.addWidget(self.ok_btn)
        layout.addWidget(self.cancel_btn)
        self.setLayout(layout)

    def getResults(self):
        if self.exec_() == QDialog.Accepted:
            val1 = int(self.val1.text())
            val2 = float(self.val2.text())
            val3 = int(self.val3.text())
            if val1 < 1 or val2 <= 0 or val2 >= 1 or val3 < 1:
                raise ValueError()
            return val1, val2, val3
        else:
            return None