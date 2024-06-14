import os
import numpy as np
from skimage import io, measure
from skimage.color import rgb2gray


raw_images_path = 'Images_2'
masked_images_path = 'Results_2'
annotations_path = 'Annotations_2'
os.makedirs(annotations_path, exist_ok=True)


def mask_to_bboxes(mask, min_area=1000):
    labeled_mask = measure.label(mask)
    regions = measure.regionprops(labeled_mask)
    bboxes = []
    for region in regions:
        if region.area >= min_area:
            minr, minc, maxr, maxc = region.bbox
            bboxes.append([minc, minr, maxc, maxr])
    return bboxes


for filename in os.listdir(raw_images_path):
    raw_image_path = os.path.join(raw_images_path, filename)
    mask_image_path = os.path.join(masked_images_path, filename)
    
    raw_image = io.imread(raw_image_path)
    mask_image = io.imread(mask_image_path)
    
    if mask_image.ndim == 3:  
        mask_image = rgb2gray(mask_image)
    
    mask_image = mask_image > 0.5  
    
    bboxes = mask_to_bboxes(mask_image)
    
    # Save annotation in YOLO format
    annotation_file = os.path.join(annotations_path, os.path.splitext(filename)[0] + '.txt')
    with open(annotation_file, 'w') as f:
        for bbox in bboxes:
            x_center = (bbox[0] + bbox[2]) / 2 / raw_image.shape[1]
            y_center = (bbox[1] + bbox[3]) / 2 / raw_image.shape[0]
            width = (bbox[2] - bbox[0]) / raw_image.shape[1]
            height = (bbox[3] - bbox[1]) / raw_image.shape[0]
            f.write(f"0 {x_center} {y_center} {width} {height}\n")