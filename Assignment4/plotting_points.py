import cv2
import matplotlib.pyplot as plt
import csv
import matplotlib.image as mpimg

# Load the image
image_path = 'IITM_map_without_background.png'  # Replace with the path to your image
# image = cv2.imread(image_path)
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# image_rgb = mpimg.imread('IITM_map_without_background.png')
img = mpimg.imread('IITM_map_without_background.png')
img_height, img_width = img.shape[:2]  # Get image dimensions


# Function to capture points without limiting the number of clicks
def capture_points(label):
    # plt.imshow(image_rgb)
    plt.figure(figsize=(img_width/100, img_height/100))  # Adjust figure size to match image size in inches

    # Plot the image at its original size
    plt.imshow(img, extent=[0, img_width, 0, img_height])

    plt.title(f"Mark points for {label}. Press Enter when done.")
    points = plt.ginput(n=-1, timeout=0)  # n=-1 allows unlimited points, ends on Enter
    labeled_points = [(x, y, label) for x, y in points]
    return labeled_points

# Mark forest areas
forest_points = capture_points('pond2')

# Combine points and save to CSV
csv_file = 'pond2.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['X', 'Y', 'Type'])  # Headers
    writer.writerows(forest_points)

print(f"Marked points saved to {csv_file}.")
