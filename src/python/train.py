from ultralytics import YOLO

def train_yolo(data_config_path, model_config_path, epochs, batch_size, img_size):
    model = YOLO(model_config_path)
    # 训练模型
    results = model.train(
        data=data_config_path,  # 数据集配置文件路径
        epochs=epochs,         # 训练的迭代次数
        batch=batch_size,      # 每个批次的图像数量
        imgsz=img_size,        # 训练图像的尺寸
        project='../../results/train',  # 保存训练结果的目录
        name='exp',            # 实验名称
        # 其他可选参数，如验证集、工作进程数等
        device='0',            # 指定设备，例如'0'表示第一个GPU，'cpu'表示CPU
        # workers=8             # 数据加载的工作进程数
    )
    return results


if __name__ == '__main__':
    data_config = '../../data/data.yaml'
    model_config = 'yolov8n.pt'
    results = train_yolo(data_config, model_config, 100, 64, 640)