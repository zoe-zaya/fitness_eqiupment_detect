import os
import sys

def rename_images(start_number=2001):
    # 获取当前文件夹路径
    current_dir = os.getcwd()
    
    # 支持的图片格式
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
    
    # 获取所有图片文件
    image_files = []
    for file in os.listdir(current_dir):
        if os.path.isfile(file):
            ext = os.path.splitext(file)[1].lower()
            if ext in image_extensions:
                image_files.append(file)
    
    if not image_files:
        print("当前文件夹中没有找到图片文件。")
        return
    
    # 按文件名排序
    image_files.sort()
    
    print(f"找到 {len(image_files)} 个图片文件:")
    for file in image_files:
        print(f"  {file}")
    
    # 询问确认
    confirm = input(f"\n是否要将这些文件重命名为从 {start_number} 开始的数字? (y/n): ").strip().lower()
    if confirm != 'y':
        print("操作已取消。")
        return
    
    # 重命名文件
    renamed_count = 0
    for i, old_name in enumerate(image_files):
        file_ext = os.path.splitext(old_name)[1]
        new_name = f"{start_number + i}{file_ext}"
        
        # 检查新文件名是否已存在
        if os.path.exists(new_name):
            print(f"错误: 文件名 {new_name} 已存在，跳过 {old_name}")
            continue
        
        try:
            os.rename(old_name, new_name)
            print(f"已重命名: {old_name} -> {new_name}")
            renamed_count += 1
        except Exception as e:
            print(f"重命名 {old_name} 时出错: {e}")
    
    print(f"\n完成! 成功重命名了 {renamed_count} 个文件。")

if __name__ == "__main__":
    # 如果需要自定义起始数字，可以修改下面的参数
    rename_images(start_number=2001)