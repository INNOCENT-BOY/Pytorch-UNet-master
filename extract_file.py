import os
import shutil

src_dir = "/home/lijiahui/data/VOCdevkit/VOC2012/SegmentationClass"
changed_dir = "/home/lijiahui/data/VOCdevkit/VOC2012/JPEGImages"
dst_dir = "/home/lijiahui/data/VOCdevkit/VOC2012/Images"
for img in os.listdir(src_dir):
    new_name = img.replace('png', 'jpg')
    src_path = os.path.join(changed_dir, new_name)
    dst_path = os.path.join(dst_dir, new_name)
    shutil.copy(src_path, dst_path)