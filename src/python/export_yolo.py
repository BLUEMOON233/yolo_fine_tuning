from ultralytics import YOLO

model = YOLO('../../results/train/exp/weights/best.pt')

model.export(format='onnx')