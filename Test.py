import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_opening, binary_closing, binary_dilation

# Replace 'your_image.jpg' with the path to your local image
image_path = 'BloodImage_00000.jpg'

# Load and preprocess the local image
image = tf.io.read_file(image_path)
image = tf.image.decode_jpeg(image)
image = tf.image.resize(image, [256, 256])
image = tf.cast(image, tf.float32) / 255.0

# Convert the image to HSV color space
image_hsv = tf.image.rgb_to_hsv(image)

# Define the lower and upper bounds for the target color in HSV space
lower_hsv = np.array([27 / 179, 20 / 255, 138 / 255], dtype=np.float32)
upper_hsv = np.array([179 / 179, 172 / 255, 255 / 255], dtype=np.float32)

# Create a mask for the target color
mask = tf.reduce_all(tf.logical_and(image_hsv >= lower_hsv, image_hsv <= upper_hsv), axis=-1)
mask = tf.cast(mask, dtype=tf.float32)

# Convert mask to numpy for morphological operations
mask_np = mask.numpy()

# Perform morphological closing followed by opening to remove small non-white areas
structure = np.ones((7, 7), dtype=np.float32)  # Increase the structuring element size
closed_mask_np = binary_closing(mask_np, structure=structure).astype(np.float32)
opened_mask_np = binary_opening(closed_mask_np, structure=structure).astype(np.float32)

# Further clean the mask by dilation to remove small non-white areas completely
cleaned_mask_np = binary_dilation(opened_mask_np, structure=structure).astype(np.float32)

# Convert cleaned mask back to tensor
cleaned_mask = tf.convert_to_tensor(cleaned_mask_np, dtype=tf.float32)

# Create a white image
white_image = tf.ones_like(image)

# Apply the cleaned mask
masked_image_with_white = image * tf.expand_dims(cleaned_mask, axis=-1) + white_image * tf.expand_dims(1 - cleaned_mask, axis=-1)

# Display the original and masked images
def display_images(original, masked):
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(original)
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.title("Highlighted Objects with White Mask")
    plt.imshow(masked)
    plt.axis('off')
    
    plt.show()

display_images(image.numpy(), masked_image_with_white.numpy())
