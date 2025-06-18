import os
import shutil
from pathlib import Path
import pandas as pd

def rename_and_upload_folders(source_dir, target_dir, product_info):
    """
    重命名并上传文件夹到指定目录
    
    Args:
        source_dir: 源文件夹目录
        target_dir: 目标网络共享目录
        product_info: 包含序号和产品名称的字典列表
    """
    # 确保目标目录存在
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # 获取源目录中的所有文件夹
    folders = sorted([f for f in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, f))],
                    key=lambda x: os.path.getctime(os.path.join(source_dir, x)))
    
    # 打印文件夹和产品信息的数量
    print(f"源目录中的文件夹数量: {len(folders)}")
    print(f"产品信息数量: {len(product_info)}")
    
    # 按顺序处理每个文件夹和对应的产品信息
    for i, (folder_name, info) in enumerate(zip(folders, product_info)):
        folder_path = os.path.join(source_dir, folder_name)
        new_folder_name = f"{info['序号']} {info['产品名称']}"
        new_folder_path = os.path.join(target_dir, new_folder_name)
        
        try:
            # 复制整个文件夹到目标目录
            shutil.copytree(folder_path, new_folder_path)
            print(f"成功处理文件夹: {folder_name} -> {new_folder_name}")
        except Exception as e:
            print(f"处理文件夹 {folder_name} 时出错: {str(e)}")
    
    # 如果还有未处理的文件夹，提示用户
    if len(folders) > len(product_info):
        print(f"\n注意：还有 {len(folders) - len(product_info)} 个文件夹未处理")
    # 如果还有未使用的产品信息，提示用户
    elif len(product_info) > len(folders):
        print(f"\n注意：还有 {len(product_info) - len(folders)} 个产品信息未使用")

def main():
    # 配置参数
    source_directory = "D:\\Downloads"  # 源文件夹目录
    target_directory = r"\\192.168.0.115\\美工文件\\四川欧特科\\【6"  # 目标网络共享目录
    
    # 从Excel文件读取产品信息
    excel_path = r"D:\\Downloads\\工作簿1.xlsx"
    # 获取所有表格名称
    xl = pd.ExcelFile(excel_path)
    print("可用的表格名称:", xl.sheet_names)
    print('--------------------------------')
    sheet_name = "倍轻松"  # 设置要读取的表格名称，可以是"Sheet1"或"Sheet2"
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    # 提取数据
    product_info = []
    for index, row in df.iloc[37:].iterrows():
        if row["默认序号"] == 40:  # 只跳过序号为40的商品
            continue
        product_info.append({
            "序号": str(row["默认序号"]).zfill(2),  # 确保序号是两位数
            "产品名称": row["对外名称"]
        })
    
    # 执行重命名和上传
    rename_and_upload_folders(source_directory, target_directory, product_info)

if __name__ == "__main__":
    main() 