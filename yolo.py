from ultralytics import YOLO 
model = YOLO("yolov8n.pt") 

results = model.train(data=r"C:\Users\Arin Swadi\OneDrive\Desktop\Sciverse\DeepLearning\custom_data.yaml", epochs=8)
