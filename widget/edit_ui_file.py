import os

file_path = os.path.join(os.path.dirname(__file__), 'Editor_ui.py')
with open(file_path, encoding='utf-8', mode='r') as f:
    lines = f.readlines()

# 找到所有的import语句结束的行号
import_end = 0
for i, line in enumerate(lines):
    if line.startswith('from') or line.startswith('import'):
        import_end = i
import_end += 1

# 在import结束的下一行插入自定义import
lines.insert(import_end, 'from .custom import MyTextEdit\n')

# 找到并替换所有的QTextEdit
for i, line in enumerate(lines):
    if 'QtWidgets.QTextEdit' in line:
        lines[i] = line.replace('QtWidgets.QTextEdit', 'MyTextEdit')

# 将更新后的代码写入文件
with open(file_path, encoding='utf-8', mode='w') as f:
    f.writelines(lines)