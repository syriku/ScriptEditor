from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import QTextEdit


class MyTextEdit(QTextEdit):
    returnPressed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            # 按下的是回车键
            print("檢測到ctrl修飾回車鍵按下")
            self.returnPressed.emit()
        else:
            super().keyPressEvent(event)
