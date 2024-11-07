from PyQt5.QtWidgets import QDialog,QLineEdit,QVBoxLayout,QPushButton,QLabel


class AntsPopup(QDialog):
    def __init__(self, parent = None, val1 = 10, val2 = 1000, val3 = 1.0, val4=2.0, val5=0.5, val6=1.0,
                 name1 = "кол-во мурваьев", name2 = "кол-во итераций", name3 = "важность феромона",
                 name4 ="важность растояния", name5="скорость испарения", name6="начальный уровень феромона",
                 max1 = 10):
        super(AntsPopup, self).__init__()
        self.max1=max1
        self.name1 = QLabel(self)
        self.name1.setText(name1)
        self.name2 = QLabel(self)
        self.name2.setText(name2)
        self.name3 = QLabel(self)
        self.name3.setText(name3)
        self.name4 = QLabel(self)
        self.name4.setText(name4)
        self.name5 = QLabel(self)
        self.name5.setText(name5)
        self.name6 = QLabel(self)
        self.name6.setText(name6)
        self.val1 = QLineEdit(self)
        self.val1.setFixedWidth(40)
        self.val1.setText(str(val1))
        self.val2 = QLineEdit(self)
        self.val2.setFixedWidth(40)
        self.val2.setText(str(val2))
        self.val3 = QLineEdit(self)
        self.val3.setFixedWidth(40)
        self.val3.setText(str(val3))
        self.val4 = QLineEdit(self)
        self.val4.setFixedWidth(40)
        self.val4.setText(str(val4))
        self.val5 = QLineEdit(self)
        self.val5.setFixedWidth(40)
        self.val5.setText(str(val5))
        self.val6 = QLineEdit(self)
        self.val6.setFixedWidth(40)
        self.val6.setText(str(val6))
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
        layout.addWidget(self.name4)
        layout.addWidget(self.val4)
        layout.addWidget(self.name5)
        layout.addWidget(self.val5)
        layout.addWidget(self.name6)
        layout.addWidget(self.val6)
        layout.addWidget(self.ok_btn)
        layout.addWidget(self.cancel_btn)
        self.setLayout(layout)

    def getResults(self):
        if self.exec_() == QDialog.Accepted:
            val1 = int(self.val1.text())
            val2 = int(self.val2.text())
            val3 = float(self.val3.text())
            val4 = float(self.val4.text())
            val5 = float(self.val5.text())
            val6 = float(self.val6.text())
            if (val1 < 1 or val1 >self.max1) or val2 < 1 or val3 < 0 or val4 < 0 or (val5 < 0 or val5 > 1) or val6 < 0:
                raise ValueError()
            return val1, val2, val3, val4, val5, val6
        else:
            return None