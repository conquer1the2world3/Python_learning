import os

# 创建一个目录中的所有文件的硬链接到另一个目录
def create_hard_links(folder, new_folder):
    # 如果番剧主文件夹不存在，创建一个
    while not os.path.exists(new_folder):
        os.mkdir(new_folder)
    # 遍历文件夹中的所有文件
    for file_name in os.listdir(folder):
        try:
            file_path = os.path.join(folder, file_name)
            # 如果是文件夹，递归调用函数
            if os.path.isdir(file_path):
                # 同时创建该文件夹,因为硬链接不能链接文件夹
                new_folder_path = os.path.join(new_folder, file_name)
                os.mkdir(new_folder_path)
                create_hard_links(file_path, new_folder_path)
            else:
                new_file_path = os.path.join(new_folder, file_name)
                # 如果文件已经存在，添加后缀“_copy{n}”,比如有多个“cover.jpg”,命名为“cover_copy1.jpg”,“cover_copy2.jpg”等
                while os.path.exists(new_file_path):
                    print(f"Renaming {file_name} to add the suffix “_copy” in {new_folder}")
                    count = 1
                    file_name_without_extension, file_extension = os.path.splitext(file_name)
                    new_file_name = f"{file_name_without_extension}_copy{count}{file_extension}"
                    count += 1
                    new_file_path = os.path.join(new_folder, new_file_name)
                    os.link(file_path, new_file_path)
                else:
                    os.link(file_path, new_file_path)
                    print(f"链接成功！快去{anime_dir}看看吧o(*￣▽￣*)ブ！")
        except (FileNotFoundError, PermissionError) as e:
            print(f"An error occurred: {str(e)}")

# Usage example
anime_name="孤独摇滚（2020）"
# NASTools设置的二级目录
category = ["动漫" , "完结动漫"]
# suffix = "CDs"
anime_dir = f"D:\TV\Anime\{category[1]}\{anime_name}"
# os.mkdir(anime_dir)
source_folder = r'D:\Media_download\[DBD-Raws][孤独摇滚！][01-12TV全集+特典映像][1080P][BDRip][HEVC-10bit][简繁外挂][FLAC][MKV]\Fonts'
new_folder = rf'{anime_dir}'
create_hard_links(source_folder, new_folder)