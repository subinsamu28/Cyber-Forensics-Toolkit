# ui/timeline_tab.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog, QLabel
)
from core.timeline_generator import generate_timeline
import os

class TimelineTab(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.info_label = QLabel("Select a directory to generate a file access timeline.")
        self.select_button = QPushButton("Choose Folder")
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)

        self.select_button.clicked.connect(self.select_folder)

        self.layout.addWidget(self.info_label)
        self.layout.addWidget(self.select_button)
        self.layout.addWidget(self.output_box)
        self.setLayout(self.layout)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Open Folder", "")
        if folder_path:
            csv_path = os.path.join(folder_path, "timeline_output.csv")
            result = generate_timeline(folder_path, csv_path)
            self.output_box.setText(result)
