import os
import glob

def delete_thumbs_db(directory):
    """
    递归删除指定目录及其子目录中的所有 Thumbs.db 文件
    
    Args:
        directory: 要搜索的目录路径
    """
    # 使用 glob 递归搜索所有 Thumbs.db 文件
    thumbs_files = glob.glob(os.path.join(directory, "**", "Thumbs.db"), recursive=True)
    
    # 删除找到的每个 Thumbs.db 文件
    for thumbs_file in thumbs_files:
        try:
            os.remove(thumbs_file)
            print(f"已删除: {thumbs_file}")
        except Exception as e:
            print(f"删除 {thumbs_file} 时出错: {str(e)}")
    
    print(f"\n总共找到并尝试删除 {len(thumbs_files)} 个 Thumbs.db 文件")

if __name__ == "__main__":
    # 设置要搜索的目录
    target_directory = r"\\192.168.0.115\美工文件\四川欧特科\【6"  # 你可以修改这个路径
    delete_thumbs_db(target_directory) 