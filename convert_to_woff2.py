from fontTools.ttLib import TTFont
import brotli
import os

def convert_fonts_in_directory(input_dir):
    for file in os.listdir(input_dir):
        if os.path.isdir(os.path.join(input_dir, file)):
            convert_fonts_in_directory(os.path.join(input_dir, file))
        if file.endswith(".otf") or file.endswith(".ttf"):
            input_file = os.path.join(input_dir, file)
            output_file = os.path.join(r'D:\文件互传\Fonts', os.path.splitext(file)[0] + ".woff2")
            convert_otf_to_woff2(input_file, output_file)

def convert_otf_to_woff2(input_file, output_file):
    # 打开 .otf 文件
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
    print('转换成功')

# 调用函数进行转换
convert_fonts_in_directory(r'D:\文件互传\Fonts')
# convert_otf_to_woff2(r'D:\文件互传\Fonts\孤独摇滚\ARYanKaiB5Ultra.otf', 'D:\文件互传\Fonts\ARYanKaiB5Ultra.woff2')