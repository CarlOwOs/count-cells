import cv2 # pip install opencv-python
import numpy as np # pip install numpy
from skimage import io # pip install scikit-image
import os 

# Load the image
project_folder = "./" # Replace with your path
image_name = "aaaa.png"
image_path = project_folder + "images/" + image_name
image = io.imread(image_path, as_gray=True)

# Initialize list to store coordinates of dead cells
dead_cells_coordinates = []

def mark_dead_cell(event, x, y, flags, param):
    """ Callback function to record mouse click positions. """
    if event == cv2.EVENT_LBUTTONDOWN:
        dead_cells_coordinates.append((x, y))
        # Perform flood fill from this point
        # Note: You may need to adjust the loDiff and upDiff values
        flood_filled = cv2.floodFill(image.copy(), None, (x, y), 0, loDiff=(10, 10, 10), upDiff=(10, 10, 10))
        param[0][:] = flood_filled[1] # Update the image with the flood fill result

# Create a window and set the mouse callback function to mark dead cells
cv2.namedWindow("Image", cv2.WINDOW_NORMAL) # WINDOW_AUTOSIZE
cv2.setMouseCallback("Image", mark_dead_cell, [image])

# Display the image and wait for user input
while True:
    cv2.imshow("Image", image) 
    key = cv2.waitKey(1) & 0xFF

    # Press 'q' to quit
    if key == ord('q'):
        break

# Close all windows
cv2.destroyAllWindows()

folder_path = project_folder + "edited/"
# Create the folder
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    
total_pixels = image.size
white_pixels = cv2.countNonZero(image)
name, extension = image_name.split(".")

# Optionally, save the modified mask to a file
cv2.imwrite(f'{folder_path}{name}_total_{total_pixels}_white_{white_pixels}.{extension}', image)
