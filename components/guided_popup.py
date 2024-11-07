from PyQt5.QtWidgets import QDialog,QLineEdit,QVBoxLayout,QPushButton,QLabel


class GuidedPopup(QDialog):
    def __init__(self, parent = None, val1 = 1000, val2 = 0.01, name1 = "кол-во итераций", name2 = ""):
        super(GuidedPopup, self).__init__()
        self.name1 = QLabel(self)
        self.name1.setText(name1)
        self.iteration = QLineEdit(self)
        self.iteration.setFixedWidth(40)
        self.iteration.setText(str(val1))
        self.name2 = QLabel(self)
        self.name2.setText(name2)
        self.fluence = QLineEdit(self)
        self.fluence.setFixedWidth(40)
        self.fluence.setText(str(val2))
        layout = QVBoxLayout()
        self.ok_btn = QPushButton("Ok", self)
        self.cancel_btn = QPushButton("Cancel", self)
        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)
        layout.addWidget(self.name1)
        layout.addWidget(self.iteration)
        layout.addWidget(self.name2)
        layout.addWidget(self.fluence)
        layout.addWidget(self.ok_btn)
        layout.addWidget(self.cancel_btn)
        self.setLayout(layout)

    def getResults(self):
        if self.exec_() == QDialog.Accepted:
            val1 = int(self.iteration.text())
            val2 = float(self.fluence.text())
            if val1 < 1 or val2 <= 0 or val2 >= 1:
                raise ValueError()
            return val1, val2
        else:
            return None