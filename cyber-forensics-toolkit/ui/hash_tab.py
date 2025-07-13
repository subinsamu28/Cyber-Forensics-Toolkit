# ui/hash_tab.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog,
    QLabel, QComboBox
)
from core.hash_checker import calculate_hashes
import os

class HashCheckerTab(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.info_label = QLabel("Select a file or folder to calculate hashes.")
        self.select_button = QPushButton("Choose File/Folder")
        self.hash_type_combo = QComboBox()
        self.hash_type_combo.addItems(["MD5", "SHA1", "SHA256"])
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)

        self.select_button.clicked.connect(self.select_path)

        self.layout.addWidget(self.info_label)
        self.layout.addWidget(self.hash_type_combo)
        self.layout.addWidget(self.select_button)
        self.layout.addWidget(self.output_box)
        self.setLayout(self.layout)

    def select_path(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")

        if file_path:
            hash_type = self.hash_type_combo.currentText()
            results = calculate_hashes(file_path, hash_type)
            self.output_box.setText("\n".join(results))
