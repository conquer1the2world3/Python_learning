import os

def generate_file_tree(directory, padding=''):
    tree = ''
    items = os.listdir(directory)
    for i, item in enumerate(sorted(items)):
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            tree += '{}├── {}\n'.format(padding, item)
            if i == len(items) - 1:
                sub_padding = padding + '    '
            else:
                sub_padding = padding + '│   '
            tree += generate_file_tree(path, padding=sub_padding)
        else:
            if i == len(items) - 1:
                tree += '{}└── {}\n'.format(padding, item)
            else:
                tree += '{}├── {}\n'.format(padding, item)
    return tree
# Example usage
directory_path = r'D:\Radio\BBC Radio'
file_tree = generate_file_tree(directory_path)
abs_directory = os.path.abspath(directory_path)
print(f"输出的file tree包含{abs_directory}的最后一级目录和其下的结构")
print(abs_directory + '\n' + file_tree)