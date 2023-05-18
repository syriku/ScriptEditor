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
        self.handler: Optional[Handler] = None
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
            self.handler = Handler(fname[0])

    @pyqtSlot()
    def on_B_create_clicked(self):
        fname = QFileDialog.getSaveFileName(self, '创建文件', "", "JSON Files (*.json)")
        if fname:
            print(f"test: 假裝完成了一次創建:{fname}")
            # 創建空文件，寫入一對[]滿足json格式
            with open(fname[0], 'w', encoding='utf-8') as f:
                f.write("[]")
            self.handler = Handler(fname[0])

    @pyqtSlot()
    def on_B_save_clicked(self):
        self.handler.save()

    @pyqtSlot()
    def on_B_save_as_clicked(self):
        fname = QFileDialog.getSaveFileName(self, '保存文件', "", "JSON Files (*.json)")
        self.handler.save(fname[0])

    @pyqtSlot()
    def insert(self):
        print("test: 假裝完成了一次插入")

    @pyqtSlot()
    def on_B_scene_clicked(self):
        ...

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     editor = ScriptEditor()
#     editor.show()
#     sys.exit(app.exec())
