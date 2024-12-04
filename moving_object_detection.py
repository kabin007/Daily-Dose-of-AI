'''
This program captures the moving object from the
 image frame applying computer vision techniques
'''


import cv2 

# Initialize the video capture object
cam = cv2.VideoCapture(0)

# Read the first frame
ret, frame1 = cam.read()

# Ensure that the frame is captured correctly
if not ret:
    print("Failed to grab the first frame")
    cam.release()
    exit()

# Convert the first frame to grayscale and blur to reduce noise
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)

while True:
    # Capture the next frame
    ret, frame2 = cam.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    # Convert the second frame to grayscale and blur it
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

    # Compute the absolute difference between the first and the second frame
    diff = cv2.absdiff(gray1, gray2)

    # Threshold the difference to get the moving parts
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    # Find contours (moving object)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # If contours are found, it means there is movement
    if len(contours) > 0:
        print('Moving object')
    else:
        print('Normal')

    # Display the frame, difference, and threshold
    cv2.imshow('Frame', frame2)
    cv2.imshow('Difference', diff)
    cv2.imshow('Threshold', thresh)

    # Update the first frame to be the current frame
    gray1 = gray2

    # Exit loop if 'q' is pressed
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release the camera and destroy all windows
cam.release()
cv2.destroyAllWindows()
