
# Hand Gesture Recognition Using MediaPipe and OpenCV

This project demonstrates real-time hand tracking and gesture recognition using OpenCV and MediaPipe. It captures video from your webcam, detects hand landmarks in real-time, and draws the hand skeleton on the video feed. The project is ideal for anyone looking to explore computer vision and gesture recognition using Python.

## Feature 

- Real-Time Hand Tracking: Utilizes MediaPipe's hand tracking solution to detect and track up to two hands simultaneously.
- Hand Landmark Detection: Extracts precise 3D hand landmarks and maps them to the video feed.
- Customizable: Adjustable parameters like the number of hands to track, detection confidence, and tracking confidence.
- Interactive: Visualizes hand landmarks and connections in real-time on your video feed.
## Prerequisites

Before running the code, ensure you have the following installed:

- Python 3.x
- OpenCV: pip install opencv-python
- MediaPipe: pip install mediapipe
## How to Run 

1. Clone or Download the repository: 

git clone https://github.com/kunal-1207/hand-gesture-recognition

cd hand-gesture-recognition

2. Install the Required Packages:

pip install -r requirements.txt

If you don’t have a requirements.txt, install manually:

pip install opencv-python mediapipe

3. Run the Script:

python hand_tracking.py

4. Interact with the Application:

- The webcam feed will open in a new window with detected hand landmarks drawn on it.
- Press the q key to close the application.



## Code Explaination

## Initialization:
- MediaPipe Hands solution is initialized with parameters to detect up to two hands, and confidence thresholds are set for detection and tracking.
- OpenCV captures video from the default webcam.

## Main Loop:
- The webcam frame is continuously captured, processed for hand detection, and displayed with overlaid hand landmarks.
- If hands are detected, the landmarks are drawn on the frame, and their coordinates are printed for debugging.

## Termination:

- The webcam feed is closed by pressing the q key, releasing the camera and destroying the OpenCV window.
## Customization

- Tracking More Hands: Adjust max_num_hands in the MediaPipe Hands initialization to track more than two hands.

- Confidence Levels: Modify min_detection_confidence and min_tracking_confidence for stricter or looser detection requirements.

- Debugging: Remove or modify the landmark coordinate printing section to fit your needs.
## Troubleshooting 

- Camera Not Detected: Ensure your webcam is correctly installed and accessible.
- Low Frame Rate: Adjust the min_detection_confidence and min_tracking_confidence to improve performance at the cost of accuracy.
## Future Enhancement 

- Gesture Recognition: Implement specific gesture recognition based on the detected landmarks.
- Hand Pose Estimation: Extend the project to estimate and classify different hand poses.
## License

[MIT](https://choosealicense.com/licenses/mit/)


