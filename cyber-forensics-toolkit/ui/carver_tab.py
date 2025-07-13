# ui/carver_tab.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog, QLabel
)
from core.file_carver import carve_files
import os

class FileCarverTab(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.info_label = QLabel("Select a raw binary file to carve JPEG, ZIP, or PDF files.")
        self.select_button = QPushButton("Choose Binary File")
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)

        self.select_button.clicked.connect(self.select_file)

        self.layout.addWidget(self.info_label)
        self.layout.addWidget(self.select_button)
        self.layout.addWidget(self.output_box)
        self.setLayout(self.layout)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if file_path:
            output_dir = os.path.join(os.path.dirname(file_path), "carved_output")
            os.makedirs(output_dir, exist_ok=True)

            results = carve_files(file_path, output_dir)
            self.output_box.setText("\n".join(results))
