import matplotlib.pyplot as plt
from skimage import io, color
import matplotlib.patches as patches

def plot_image_with_bboxes(image_path, annotation_path):
    image = io.imread(image_path)
    fig, ax = plt.subplots(1)
    ax.imshow(image)

    with open(annotation_path, 'r') as f:
        for line in f:
            label, x_center, y_center, width, height = map(float, line.strip().split())
            x_center *= image.shape[1]
            y_center *= image.shape[0]
            width *= image.shape[1]
            height *= image.shape[0]
            x_min = x_center - width / 2
            y_min = y_center - height / 2
            rect = patches.Rectangle((x_min, y_min), width, height, linewidth=1, edgecolor='r', facecolor='none')
            ax.add_patch(rect)

    plt.show()


test_image_path = 'Images/BloodImage_00000.jpg'
test_annotation_path = 'Annotations/BloodImage_00000.txt'
plot_image_with_bboxes(test_image_path, test_annotation_path)