import cv2

# Initialize the camera objects
cameras = [
    cv2.VideoCapture(0),  # Camera 1
    # cv2.VideoCapture(1),  # Camera 2
    # cv2.VideoCapture(2),  # Camera 3
    # cv2.VideoCapture(3),  # Camera 4
    # cv2.VideoCapture(4)  # Camera 5
]

# Define the reference color (white in this case)
reference_color = (255, 255, 255)


while True:
    # Read frames from each camera
    frames = []
    for camera in cameras:
        ret, frame = camera.read()
        frames.append(frame)



    # Perform color change detection for each camera
    for i, frame in enumerate(frames):
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Calculate the absolute difference between the current frame and reference color
        diff = cv2.absdiff(gray, reference_color[0])

        # Threshold the difference image
        _, threshold = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

        # Find contours in the thresholded image
        contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Check if any contour is detected
        if len(contours) > 0:
            # Perform additional actions based on your requirements
            # For example, you can draw bounding boxes around the contours
            for contour in contours:
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


    # Show the frames from each camera
    cv2.imshow('Camera 1', frames[0])
    # cv2.imshow('Camera 2', frames[1])
    # cv2.imshow('Camera 3', frames[2])
    # cv2.imshow('Camera 4', frames[3])
    # cv2.imshow('Camera 5', frames[4])

 # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# Release the camera objects and close the windows
for camera in cameras:
    camera.release()
cv2.destroyAllWindows()