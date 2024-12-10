import xml.etree.ElementTree as ET
import shutil
import os

classes = ["aeroplane", "bicycle", "bird", "boat",
            "bottle", "bus", "car", "cat", "chair", "cow",
            "diningtable", "dog", "horse", "motorbike", "person",
            "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
class_to_ind = {cls: i for i, cls in enumerate(classes)}  # 类别到索引的映射

PATH = '../../pascalvoc/VOCdevkit/VOC2007/'
OUTPUT_PATH = '../../data/'

# 转换标注
def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

# 解析XML并转换标注
def convert_annotation(image_id, tar_label):
    in_file = open(PATH + f'Annotations/{image_id}.xml', encoding='UTF-8')
    out_file = open(OUTPUT_PATH + f'{tar_label}/labels/{image_id}.txt', 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = class_to_ind[cls]
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)

        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')



def copy_pic(image_id, tar_label):
    source_path = PATH + f'JPEGImages/{image_id}.jpg'
    destination_path = OUTPUT_PATH + f'{tar_label}/images/{image_id}.jpg'
    if os.path.exists(source_path):
        shutil.copy(source_path, destination_path)
        # print(f"文件已成功复制到 {destination_path}")
    else:
        print('error with', image_id)


if __name__ == '__main__':
    # tar_labels = ['train', 'test', 'val']
    # for tar_label in tar_labels:
    #     image_ids = open(PATH + f'ImageSets/Main/{tar_label}.txt').read().strip().split()
    #     for image_id in image_ids:
    #         convert_annotation(image_id, tar_label)
    #         copy_pic(image_id, tar_label)
    print(class_to_ind)
    for cls in classes:
        print(f'{class_to_ind[cls]}:{cls}')