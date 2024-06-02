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
directory_path = r'D:\TV\Anime\完结动漫\孤独摇滚（2020）1\Fonts\fonts'
file_tree = generate_file_tree(directory_path)
last_level_directory = os.path.basename(directory_path)
print(f"输出的file tree包含{last_level_directory}的最后一级目录和其下的结构")
print(last_level_directory + '\n' + file_tree)