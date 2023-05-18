import json
from typing import Optional, List

from .Scene import Scene


class Handler(object):
    """剧本文件的格式管理，保存和读取"""

    def __init__(self, path=None):
        self.path = path
        self.data: Optional[List[Scene]] = None  # data总是一个可以转换为json字符串的对象
        if not path:
            print("未指定路径，创建空对象")
        else:
            print(f"读取文件:{path}")
            self.load()

    def save(self, path=None):
        if not path:
            path = self.path
        if self.data and path:
            # data转换为json格式字符串，存入path

            json_str = json.dumps(self.data, indent=4, ensure_ascii=False)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(json_str)
                print("保存完成")

    def load(self):
        if self.path:
            # 从path读入json格式字符串，转换为data
            with open(self.path, 'r', encoding='utf-8') as f:
                json_str = f.read()
                json_object = json.loads(json_str)
            print("json读取完成")
            for scene in json_object:
                new_scene = Scene(script=scene)
