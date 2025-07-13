import sys
from PyQt5.QtWidgets import QApplication, QTabWidget, QMainWindow
from PyQt5.QtGui import QIcon
from ui.extractor_tab import MetadataExtractorTab
from ui.carver_tab import FileCarverTab
from ui.recovery_tab import FileRecoveryTab
from ui.hash_tab import HashCheckerTab
from ui.timeline_tab import TimelineTab
import os

class ForensicsMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cyber Forensics Toolkit")
        self.setGeometry(100, 100, 1000, 700)
        self.setWindowIcon(QIcon("assets/logo.png"))

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tabs.addTab(MetadataExtractorTab(), "Metadata Extractor")
        self.tabs.addTab(FileCarverTab(), "File Carver")
        self.tabs.addTab(FileRecoveryTab(), "Deleted File Recovery")
        self.tabs.addTab(HashCheckerTab(), "Hash Checker")
        self.tabs.addTab(TimelineTab(), "Timeline Generator")

def main():
    app = QApplication(sys.argv)

    # Apply custom QSS stylesheet
    qss_path = os.path.join("assets", "darkstyle.qss")
    if os.path.exists(qss_path):
        with open(qss_path, "r") as f:
            app.setStyleSheet(f.read())

    window = ForensicsMainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
