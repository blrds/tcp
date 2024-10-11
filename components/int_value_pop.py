from PyQt5.QtWidgets import QDialog,QLineEdit,QVBoxLayout,QPushButton


class IntValuePopup(QDialog):
    def __init__(self, parent = None,):
        super(IntValuePopup, self).__init__()
        self.value = QLineEdit(self)
        self.value.setFixedWidth(40)
        layout = QVBoxLayout()
        self.ok_btn = QPushButton("Ok", self)
        self.cancel_btn = QPushButton("Cancel", self)
        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)
        layout.addWidget(self.value)
        layout.addWidget(self.ok_btn)
        layout.addWidget(self.cancel_btn)
        self.setLayout(layout)

    def getResults(self):
        if self.exec_() == QDialog.Accepted:
            val1 = int(self.value.text())
            if val1 < 1:
                raise ValueError()
            return val1
        else:
            return None