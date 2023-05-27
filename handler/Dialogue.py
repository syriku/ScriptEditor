from typing import Dict, List


class Dialogue(object):
    def __init__(self, script: Dict[str, List[str]]):
        # self.speaker = script.get("Speaker", "")
        # self.dialogue = script.get("Dialogue", [])
        # self.choices = script.get("Choice", [])
        # self.introduction = self.dialogue[0][:20]
        print(script)
        self.speaker: str = list(script.keys())[0]
        dialogues: list = script[self.speaker]
        self.dialogue: str = dialogues[0]
        self.choices: List[str] = []
        if len(dialogues) > 1:
            self.choices = dialogues[1:]
        self.introduction = self.dialogue[:20]
        print("转换完成。", self.speaker, self.dialogue, self.choices, self.introduction)

    # def __str__(self):
    #     dialogue_str = "\n".join(self.dialogue)
    #     choices_str = "\n".join(self.choices)
    #     return f"Speaker: {self.speaker}\nDialogue: {dialogue_str}\nChoices: {choices_str}"
    def __dict__(self):
        """将数据打包为dict"""
        return {self.speaker: [self.dialogue] + self.choices}
