# ui/extractor_tab.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog, QLabel
)
from core.metadata_extractor import extract_metadata

class MetadataExtractorTab(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.info_label = QLabel("Select a file to extract metadata (PDF, DOCX, Image, ZIP)")
        self.select_button = QPushButton("Choose File")
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
            metadata = extract_metadata(file_path)
            self.output_box.setText(metadata)
