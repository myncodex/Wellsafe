import cv2
# Load the video or image from the source
source = cv2.VideoCapture('video.mp4')

# Create a background subtractor object
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

while True:
    # Read the frame from the video or image source
    ret, frame = source.read()
    if not ret:
        break

    # Apply background subtraction
    fg_mask = bg_subtractor.apply(frame)

    # Apply morphological operations to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)

    # Find contours in the foreground mask
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Calculate the contour area
        area = cv2.contourArea(contour)

        # Filter out small contours
        if area > 1000:
            # Get the bounding box coordinates
            x, y, w, h = cv2.boundingRect(contour)

            # Draw a rectangle around the detected human
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Human Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video source and destroy windows
source.release()
cv2.destroyAllWindows()