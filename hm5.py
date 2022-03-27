# дерево каталога 
import os


def read_dir(folder):
    for root, dirs, files in os.walk(folder):
        # print(root, dirs, fules)
        level = root.count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}[{os.path.basename(root)}]')
        sub_indent = ' ' * 4 * (level + 1)
        # print(root, fules, level, indent, sub_indent)
        for file in files:
            print(f'{sub_indent}{file}')
        
        
read_dir('files')