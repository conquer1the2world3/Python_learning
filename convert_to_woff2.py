from fontTools.ttLib import TTFont
import brotli
import os

def convert_fonts_in_directory(input_dir):
    for file in os.listdir(input_dir):
        if os.path.isdir(os.path.join(input_dir, file)):
            convert_fonts_in_directory(os.path.join(input_dir, file))
            # 如果文件后缀是.otf/.ttf
        elif file.lower().endswith((".otf", ".ttf")):
            input_file = os.path.join(input_dir, file)
            output_file = os.path.join(output_dir, os.path.splitext(file)[0] + ".woff2")
            convert_otf_to_woff2(input_file, output_file)
        else:
            print(f"文件{file}不是.otf/.ttf文件")

def convert_otf_to_woff2(input_file, output_file):
    # 打开 字体文件
    font = TTFont(input_file)

    # 将字体保存为 .woff2 文件
    font.save(output_file, 'woff2')

    # 压缩 .woff2 文件
    with open(output_file, 'rb') as f:
        woff2_data = f.read()

    compressed_data = brotli.compress(woff2_data)

    # 将压缩后的数据保存为 .woff2 文件
    with open(output_file, 'wb') as f:
        f.write(compressed_data)
    print(f'转换成功，他们在{output_dir}静悄悄地等你了哦！(*^▽^*)')

# 输入和输出目录 
input_dir = r'D:\文件互传\Fonts\1'
output_dir = r'D:\文件互传\Fonts\1'
# 调用函数进行转换
convert_fonts_in_directory(input_dir)