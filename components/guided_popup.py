from PyQt5.QtWidgets import QDialog,QLineEdit,QVBoxLayout,QPushButton


class GuidedPopup(QDialog):
    def __init__(self, parent = None,):
        super(GuidedPopup, self).__init__()
        self.iteration = QLineEdit(self)
        self.iteration.setFixedWidth(40)
        self.fluence = QLineEdit(self)
        self.fluence.setFixedWidth(40)
        layout = QVBoxLayout()
        self.ok_btn = QPushButton("Ok", self)
        self.cancel_btn = QPushButton("Cancel", self)
        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)
        layout.addWidget(self.iteration)
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