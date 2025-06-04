import os
import subliminal

# 配置文件路径
anime_folder = r'D:\TV\Anime\完结动漫\小马宝莉：友谊就是魔法 (2010)\Season 1'  # 将此替换为您的动漫文件夹路径
subtitle_language = 'zho'  # 英文字幕的语言代码

# 遍历文件夹中的所有视频文件
for file in os.listdir(anime_folder):
    if file.endswith(('.mp4', '.mkv', '.avi')):  # 根据需要添加更多视频格式
        video_path = os.path.join(anime_folder, file)
        print(f"Searching subtitles for {file}...")

        # 使用subliminal库下载字幕
        try:
            video = subliminal.scan_video(video_path)
            subtitles = subliminal.download_best_subtitles([video], {subtitle_language})
            if subtitles[video]:
                subtitle_file = subtitles[video][0].get_path()
                print(f"Subtitles downloaded: {subtitle_file}")
            else:
                print("No subtitles found.")
        except Exception as e:
            print(f"Error downloading subtitles: {e}")