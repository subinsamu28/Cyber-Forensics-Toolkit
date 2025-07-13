# ui/recovery_tab.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog, QLabel
)
from core.file_recovery import recover_deleted_files
import os

class FileRecoveryTab(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.info_label = QLabel("Select a disk image (FAT/NTFS) to recover deleted files.")
        self.select_button = QPushButton("Choose Disk Image")
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)

        self.select_button.clicked.connect(self.select_file)

        self.layout.addWidget(self.info_label)
        self.layout.addWidget(self.select_button)
        self.layout.addWidget(self.output_box)
        self.setLayout(self.layout)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Disk Image", "", "Image Files (*.img *.dd *.raw);;All Files (*)")
        if file_path:
            output_dir = os.path.join(os.path.dirname(file_path), "recovered_files")
            os.makedirs(output_dir, exist_ok=True)

            results = recover_deleted_files(file_path, output_dir)
            self.output_box.setText("\n".join(results))
