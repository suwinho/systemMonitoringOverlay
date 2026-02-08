import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt, QTimer
import engine


class IntelOverlay(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(50,50,400,500)

        self.label = QLabel("Collecting data...", self)
        self.label.setStyleSheet(
            "color: #00FF00; font-family: Consolas; font-size: 14px; background: rgba(0,0,0,150); padding: 10px; border-radius: 5px;")
        self.label.adjustSize()
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh)
        self.timer.start(1000)

    def refresh(self):
        stats = engine.get_system_stats()
        procs = engine.get_top_processes()

        text = ""
        text += f"CORE USAGE: {stats['cpu_usage']}%\nRAM: {stats['ram_usage']}%\n\n"
        text += "TOP PROCESSES (CPU):\n"

        for p in procs:
            text += f"[{p['pid']}] {p['name'][:15]}: {p['cpu_percent']}%\n"

        text += "\n[Press Ctrl+C in Terminal to Exit]"
        self.label.setText(text)
        self.label.adjustSize()


app = QApplication(sys.argv)
ov = IntelOverlay()
ov.show()
sys.exit(app.exec_())