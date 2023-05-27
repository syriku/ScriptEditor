from typing import List, Dict

from .Dialogue import Dialogue


class Scene(object):

    def __init__(self, name=None, script=None):
        self.dialogues: List[Dialogue] = []
        if name and not script:
            self.name = name
            return
        if script:
            self.load(script)
            return
        raise AttributeError("非法初始化参数")

    def load(self, script: dict):
        self.name = script.get("Scene", "")
        dialogues = script.get("Dialogues", [])
        for dialogue in dialogues:
            dialogue_object = Dialogue(dialogue)
            # 如果两句台词的开头字符相同，会导致覆盖。可能会有问题
            self.dialogues.append(dialogue_object)
        print(f"转换完成。{self.name}: {self.dialogues}")

    def __dict__(self):
        """将Scene对象打包为dict，便于转换成json字符串"""
        return {"Scene": self.name, "Dialogues": self.dialogues}

    def list_dialogues(self):
        ...
