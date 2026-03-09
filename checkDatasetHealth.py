import os
from PIL import Image

def check_dataset_health(image_dir):
    """
    检查数据集中是否存在损坏或尺寸为 0 的图片
    符合任务书对'高质量数据集'的要求
    """
    bad_files = []
    valid_count = 0
    
    print(f"开始检查目录：{image_dir}")
    
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                file_path = os.path.join(root, file)
                try:
                    with Image.open(file_path) as img:
                        width, height = img.size
                        if width == 0 or height == 0:
                            bad_files.append((file_path, "尺寸为 0"))
                        else:
                            valid_count += 1
                except Exception as e:
                    bad_files.append((file_path, f"无法读取：{str(e)}"))
    
    print(f"检查完成。有效图片：{valid_count} 张")
    if bad_files:
        print(f"发现 {len(bad_files)} 张损坏图片：")
        for path, reason in bad_files:
            print(f"  - {path} ({reason})")
        print("\n建议：删除上述损坏文件，并补充新图片以满足 500 张指标。")
    else:
        print("数据集健康，无损坏图片。")

if __name__ == "__main__":
    # 请修改为您的实际数据集路径
    # 确保路径不包含中文
    dataset_path = r"D:\fitness\fitness_equipment\images\val" 
    check_dataset_health(dataset_path)