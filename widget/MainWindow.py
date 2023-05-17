# coding:utf-8
import sys
from typing import Optional

from PyQt6.QtCore import pyqtSlot, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from .Editor_ui import Ui_ScriptEditor
from handler.Handler import Handler


class ScriptEditor(QMainWindow, Ui_ScriptEditor):
    def __init__(self):
        super().__init__()
        self._handler: Optional[Handler] = None
        self.setupUi(self)
        self.init_signal()

    def init_signal(self):
        self.T_text.returnPressed.connect(self.insert)
        self.B_insert.clicked.connect(self.insert)

    @pyqtSlot()
    def on_B_open_clicked(self):
        fname = QFileDialog.getOpenFileName(self, '打开文件', "", "JSON Files (*.json)")
        if fname:
            print(f"test: 假裝完成了一次打開:{fname}")

    @pyqtSlot()
    def on_B_create_clicked(self):
        fname = QFileDialog.getSaveFileName(self, '创建文件', "", "JSON Files (*.json)")
        if fname:
            print(f"test: 假裝完成了一次創建:{fname}")

    @pyqtSlot()
    def insert(self):
        print("test: 假裝完成了一次插入")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     editor = ScriptEditor()
#     editor.show()
#     sys.exit(app.exec())
