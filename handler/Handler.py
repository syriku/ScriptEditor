import json
from typing import Optional


class Handler(object):
    """剧本文件的格式管理，保存和读取"""

    def __init__(self, path=None):
        self.path = path
        self.data = None  # data总是一个可以转换为json字符串的对象

    def save(self):
        if self.data and self.path:
            # data转换为json格式字符串，存入path

            json_str = json.dumps(self.data, indent=4, ensure_ascii=False)
            with open(self.path, 'w', encoding='utf-8') as f:
                f.write(json_str)

    def load(self):
        if self.path:
            # 从path读入json格式字符串，转换为data
            with open(self.path, 'r', encoding='utf-8') as f:
                json_str = f.read()
                self.data = json.loads(json_str)