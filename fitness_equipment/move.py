import os
import random
import shutil

def split_and_move_images():
    # 目标文件夹路径
    train_path = r"D:\fitness\fitness_dataset_raw\images\train"
    val_path = r"D:\fitness\fitness_dataset_raw\images\val"
    test_path = r"D:\fitness\fitness_dataset_raw\images\test"
    
    # 支持的图片格式
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
    
    # 获取当前文件夹中的所有图片文件
    current_dir = os.getcwd()
    all_images = []
    
    for file in os.listdir(current_dir):
        if os.path.isfile(file):
            ext = os.path.splitext(file)[1].lower()
            if ext in image_extensions:
                all_images.append(file)
    
    if not all_images:
        print("当前文件夹中没有找到图片文件。")
        return
    
    print(f"找到 {len(all_images)} 个图片文件。")
    
    # 随机打乱文件列表
    random.shuffle(all_images)
    
    # 计算划分数量
    total = len(all_images)
    train_count = int(total * 0.7)
    val_count = int(total * 0.2)
    test_count = total - train_count - val_count
    
    # 划分文件列表
    train_files = all_images[:train_count]
    val_files = all_images[train_count:train_count + val_count]
    test_files = all_images[train_count + val_count:]
    
    print(f"\n划分结果:")
    print(f"训练集 (train): {len(train_files)} 个文件 ({len(train_files)/total*100:.1f}%)")
    print(f"验证集 (val): {len(val_files)} 个文件 ({len(val_files)/total*100:.1f}%)")
    print(f"测试集 (test): {len(test_files)} 个文件 ({len(test_files)/total*100:.1f}%)")
    
    # 显示划分的文件
    print(f"\n训练集文件: {train_files}")
    print(f"验证集文件: {val_files}")
    print(f"测试集文件: {test_files}")
    
    # 确认操作
    confirm = input(f"\n确认按以上划分移动文件? (y/n): ").strip().lower()
    if confirm != 'y':
        print("操作已取消。")
        return
    
    # 创建目标文件夹（如果不存在）
    for path in [train_path, val_path, test_path]:
        os.makedirs(path, exist_ok=True)
    
    # 移动文件
    moved_count = 0
    
    for file_list, target_dir in [(train_files, train_path), (val_files, val_path), (test_files, test_path)]:
        for file_name in file_list:
            src_path = os.path.join(current_dir, file_name)
            dst_path = os.path.join(target_dir, file_name)
            
            try:
                shutil.move(src_path, dst_path)
                moved_count += 1
                # print(f"已移动: {file_name} -> {target_dir}")
            except Exception as e:
                print(f"移动 {file_name} 时出错: {e}")
    
    print(f"\n完成! 成功移动了 {moved_count} 个文件。")
    print(f"文件位置:")
    print(f"  训练集: {train_path}")
    print(f"  验证集: {val_path}")
    print(f"  测试集: {test_path}")

if __name__ == "__main__":
    split_and_move_images()