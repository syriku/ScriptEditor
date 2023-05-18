import json
from typing import Optional, List, Dict

from .Scene import Scene


class Handler(object):
    """剧本文件的格式管理，保存和读取"""

    def __init__(self, path=None):
        self.path = path
        self.data = FakeDict(Scene)
        self.loaded = False
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
            print(self.data.keys())
            print(self.data.__dict__())
            print(self.data[self.data.keys()[0]])
            json_str = json.dumps(self.data, default=lambda x: (x.__dict__() if not isinstance(x, FakeDict)
                                                                else x.values()),
                                  indent=4, ensure_ascii=False)
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
                self.data.insert(new_scene.name, new_scene)

            self.loaded = True

    def new_scene(self, name, index, fore=False):
        assert self.loaded, "no file loaded"
        # 为了保证索引顺序，Dict需要是有序的（新版本），旧版本Python运行请改为ordereddict
        self.data.insert(name, Scene(name), (index + 1) if fore else index)


class FakeDict(object):

    def __init__(self, tov):
        self.items = []
        self.type = tov

    def __dict__(self):
        return dict(self.items)

    def __getitem__(self, item):
        for key, value in self.items:
            if key == item:
                return value

    def keys(self):
        return [key for key, _ in self.items]

    def values(self):
        return [value for _, value in self.items]

    def insert(self, key, value, index=-1):
        assert isinstance(value, self.type), TypeError(f"value:{value} that try to insert is not {self.type}")
        assert index >= -1, ValueError("index cannot be negative.")
        if index == -1:
            self.items.append([key, value])
        else:
            self.items.insert(index, [key, value])
