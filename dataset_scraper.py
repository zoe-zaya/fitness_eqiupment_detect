import os
import time
from icrawler.builtin import BingImageCrawler

# 根据任务书要求，定义不少于 20 类健身器材
# 这些类别将作为 YOLO 训练时的 class names
FITNESS_CATEGORIES = [
    "Treadmill", "Cross Trainer", "Indoor Cycling Bike", "Rowing Machine", "Stair Climber",
    "Smith Machine", "Cable Crossover Machine", "Leg Press Machine", "Leg Extension Machine",
    "Leg Curl Machine", "Chest Press Machine", "Lat Pulldown Machine", "Seated Row Machine",
    "Shoulder Press Machine", "Abdominal Crunch Machine", "Hip Abductor Adductor Machine",
    "Barbell", "Weight Plates", "Dumbbells", "Kettlebell", "Bench Press",
    "Power Rack", "Yoga Mat", "TRX Suspension Trainer"
]

def download_category_images(category, output_dir, max_num=100):
    """
    针对单个类别进行图片爬取
    :param category: 器材英文名称 (搜索关键词)
    :param output_dir: 保存根目录
    :param max_num: 该类计划下载的数量
    """
    # 为每个类别创建独立文件夹，方便后续标注
    category_dir = os.path.join(output_dir, category.replace(" ", "_"))
    if not os.path.exists(category_dir):
        os.makedirs(category_dir)
    
    print(f"开始采集类别：{category} -> 保存至：{category_dir}")
    
    # 配置 Bing 图片爬虫
    # storage 指定保存路径，site 指定搜索引擎
    crawler = BingImageCrawler(storage={'root_dir': category_dir})
    
    try:
        # filters 可以限制图片大小，确保高质量 (符合任务书"高质量标注图像"要求)
        # min_size=(200, 200) 确保图片不至于太小
        crawler.crawl(
            filters=dict(size = "large"),
            keyword=category, 
            max_num=max_num, 
            file_idx_offset=0
        )
        print(f"类别 {category} 采集完成。")
    except Exception as e:
        print(f"类别 {category} 采集失败：{e}")
    
    # 礼貌性延迟，避免 IP 被封禁 (符合道德规范)
    time.sleep(5)

def main():
    # 数据集根目录
    root_dataset_dir = "./fitness_dataset_raw"
    if not os.path.exists(root_dataset_dir):
        os.makedirs(root_dataset_dir)
    
    print(f"=== 开始构建健身器材数据集 (目标：{len(FITNESS_CATEGORIES)} 类) ===")
    
    # 遍历每个类别进行采集
    # 每类 30 张 * 20 类 = 600 张，满足任务书≥500 张的要求
    for idx, category in enumerate(FITNESS_CATEGORIES):
        print(f"[{idx+1}/{len(FITNESS_CATEGORIES)}] 处理中...")
        download_category_images(category, root_dataset_dir, max_num=100)
        
    print("=== 所有类别采集完毕 ===")
    print(f"数据已保存至：{os.path.abspath(root_dataset_dir)}")
    print("下一步请使用 LabelImg 进行标注，并划分为 train/val/test 集。")

if __name__ == "__main__":
    main()