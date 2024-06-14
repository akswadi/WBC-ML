import os
import cv2
from ultralytics import YOLO

train15_dir = r'C:\Users\Arin Swadi\OneDrive\Desktop\Sciverse\DeepLearning\runs\detect\train15\weights'
best_model_path = os.path.join(train15_dir, 'best.pt')

model = YOLO(best_model_path)

image_dir = r'C:\Users\Arin Swadi\OneDrive\Desktop\Sciverse\DeepLearning\datasets\dataset\images\test'
output_dir = r'C:\Users\Arin Swadi\OneDrive\Desktop\Sciverse\DeepLearning\datasets\dataset\images\output_2'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

image_paths = [os.path.join(image_dir, img) for img in os.listdir(image_dir) if img.endswith(('jpg', 'jpeg','png'))]

results = model(image_paths)

for i, result in enumerate(results):
    result_image = result.plot()
    result_path = os.path.join(output_dir, f'annotated_{i}.jpg')
    cv2.imwrite(result_path, result_image)
