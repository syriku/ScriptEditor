from .Dialogue import Dialogue


class Scene(object):

    def __init__(self, name=None, script=None):
        if name and not script:
            self.name = name
            return
        if script:
            self.dialogues = []
            self.load(script)
            return
        raise AttributeError("非法初始化参数")

    def load(self, script: dict):
        self.name = script.get("Scene", "")
        dialogues = script.get("Dialogues", [])
        for dialogue in dialogues:
            self.dialogues.append(Dialogue(dialogue))
        print(f"转换完成。{self.name}: {self.dialogues}")

    def __str__(self):
        ...
