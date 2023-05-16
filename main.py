# coding:utf-8
import sys

from PyQt6.QtWidgets import QApplication

from widget.MainWindow import ScriptEditor


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = ScriptEditor()
    editor.show()
    sys.exit(app.exec())