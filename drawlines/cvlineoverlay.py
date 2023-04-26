import cv2
import numpy as np
import pyautogui
import time

# Wait for some time to allow the user to switch to the window they want to capture, waits 10 seconds by default
time.sleep(10)
# Take a screenshot
screenshot = pyautogui.screenshot()
# Convert the screenshot to a NumPy array
screenshot = np.array(screenshot)
# Convert the screenshot to grayscale
gray = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
# Apply histogram equalization
equ = cv2.equalizeHist(gray)
# Apply Canny edge detection with adjusted parameters
edges = cv2.Canny(equ, 50, 150, apertureSize=3)
# Find contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Draw red lines around the edges of the screenshot
cv2.drawContours(screenshot, contours, -1, (0, 0, 255), 2)
# Display the screenshot with red lines around the edges
cv2.imshow('Screenshot', screenshot)
# Wait for user input
key = cv2.waitKey(0)
# Exit the program
cv2.destroyAllWindows()
