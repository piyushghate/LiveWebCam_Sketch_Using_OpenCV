import cv2
import numpy as np

# Function
def sketch(image):
    # to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Cleaning image using GaussianBlur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    
    # get the edges
    canny_edges = cv2.Canny(img_gray_blur, 70, 30)
    
    # invert binary threshold
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask


# Initialize webcam object
# Image collected from WebCam is stored in frame
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Our Live Sketcher', sketch(frame))
    #cv2.imshow('Our Live Sketcher', frame)
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break
        
# Release camera and close windows
cap.release()
cv2.destroyAllWindows()
