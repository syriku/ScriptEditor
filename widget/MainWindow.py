# coding:utf-8
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Editor_ui import Ui_ScriptEditor


class ScriptEditor(QMainWindow, Ui_ScriptEditor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = ScriptEditor()
    editor.show()
    sys.exit(app.exec())
