from PyQt5.QtWidgets import QWidget,QTextEdit,QVBoxLayout,QPushButton,QCheckBox

class AlgorithmMenu(QWidget):
    def __init__(self,cfg, parent=None):
        super().__init__(parent)

        self.parent = parent
        layout = QVBoxLayout()
        all_paths = QPushButton(cfg['text']['all_paths_btn_text'])
        all_paths.clicked.connect(self.calc_all_paths)
        layout.addWidget(all_paths)
        brute_force_button = QPushButton(cfg['text']['bruteforce_btn_text'])
        brute_force_button.clicked.connect(self.calc_with_brute_force)
        layout.addWidget(brute_force_button)
        greedy_button = QPushButton(cfg['text']['greedy_btn_text'])
        greedy_button.clicked.connect(self.calc_with_greedy_search)
        layout.addWidget(greedy_button)
        dp_button = QPushButton(cfg['text']['dp_btn_text'])
        dp_button.clicked.connect(self.calc_with_dynamic_programming)
        layout.addWidget(dp_button)
        branch_and_bound_btn = QPushButton(cfg['text']['branch_and_bound_btn_text'])
        branch_and_bound_btn.clicked.connect(self.calc_with_branch_and_bound)
        layout.addWidget(branch_and_bound_btn)
        splitter = QPushButton()
        splitter.setFixedHeight(5)
        splitter.setStyleSheet("background-color: black")
        layout.addWidget(splitter)
        self.converegence = QCheckBox()
        self.converegence.setText("Построить график")
        layout.addWidget(self.converegence)
        ss_button = QPushButton(cfg['text']['ss_btn_text'])
        ss_button.clicked.connect(self.calc_with_simple_search)
        layout.addWidget(ss_button)
        rs_button = QPushButton(cfg['text']['rs_btn_text'])
        rs_button.clicked.connect(self.calc_with_guided_search)
        layout.addWidget(rs_button)
        srs_button = QPushButton(cfg['text']['srs_btn_text'])
        srs_button.clicked.connect(self.calc_with_smart_random_search)
        layout.addWidget(srs_button)
        sa_button = QPushButton(cfg['text']['sa_btn_text'])
        sa_button.clicked.connect(self.calc_with_annealing)
        layout.addWidget(sa_button)
        ant_button = QPushButton(cfg['text']['ant_btn_text'])
        ant_button.clicked.connect(self.calc_with_ants)
        layout.addWidget(ant_button)
        gen_button = QPushButton(cfg['text']['gen_btn_text'])
        gen_button.clicked.connect(self.calc_with_gen)
        layout.addWidget(gen_button)

        self.setLayout(layout)


    def calc_all_paths(self):
        self.parent.calc_all_paths()

    def calc_with_brute_force(self):
        self.parent.calc_with_brute_force()

    def calc_with_greedy_search(self):
        self.parent.calc_with_greedy_search()

    def calc_with_dynamic_programming(self):
        self.parent.calc_with_dynamic_programming()

    def calc_with_simple_search(self):
        self.parent.calc_with_simple_search(isCon = self.converegence.checkState())

    def calc_with_guided_search(self):
        self.parent.calc_with_guided_search(isCon = self.converegence.checkState())

    def calc_with_smart_random_search(self):
        self.parent.calc_with_smart_random_search(isCon = self.converegence.checkState())

    def calc_with_annealing(self):
        self.parent.calc_with_annealing(isCon = self.converegence.checkState())

    def calc_with_ants(self):
        self.parent.calc_with_ants(isCon = self.converegence.checkState())
    
    def calc_with_gen(self):
        self.parent.calc_with_gen(isCon = self.converegence.checkState())

    def calc_with_branch_and_bound(self):
        self.parent.calc_with_branch_and_bound()