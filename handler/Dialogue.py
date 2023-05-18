
class Dialogue(object):
    def __init__(self, script: dict):
        self.speaker = script.get("Speaker", "")
        self.dialogue = script.get("Dialogue", [])
        self.choices = script.get("Choice", [])
        self.introduction = self.dialogue[0][:20]

    # def __str__(self):
    #     dialogue_str = "\n".join(self.dialogue)
    #     choices_str = "\n".join(self.choices)
    #     return f"Speaker: {self.speaker}\nDialogue: {dialogue_str}\nChoices: {choices_str}"
