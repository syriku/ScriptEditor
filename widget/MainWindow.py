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
            self.update_scene()

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
    def on_B_scene_forward_clicked(self):
        index = self.CB_scene.currentIndex()
        self.handler.new_scene(self.LE_scene.text(), index, True)
        self.update_scene(index + 1)

    @pyqtSlot()
    def on_B_scene_backward_clicked(self):
        index = self.CB_scene.currentIndex()
        self.handler.new_scene(self.LE_scene.text(), index, False)
        self.update_scene(index)

    def update_scene(self, index=0):
        """更新场景列表LW_scene"""
        self.CB_scene.blockSignals(True)
        self.CB_scene.clear()
        self.CB_scene.addItems(self.handler.data.keys())
        self.CB_scene.setCurrentIndex(index)
        self.CB_scene.blockSignals(False)

    def update_dialogues(self):
        """更新对话列表LW_dialogue"""
        self.LW_dialogue.blockSignals(True)
        ...

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     editor = ScriptEditor()
#     editor.show()
#     sys.exit(app.exec())
