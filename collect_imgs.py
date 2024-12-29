import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3  # Update as needed
dataset_size = 100  # Number of images per class

# Try opening the camera (start with index 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to access the camera. Please check the camera index or connection.")
    exit()

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print(f'Collecting data for class {j}')
    print('Press "Q" to start collecting images for this class.')

    # Display message until user presses 'Q'
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read from camera.")
            break

        cv2.putText(frame, 'Ready? Press "Q"!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Wait for 'Q' key press
            break

    # Collect images for the class
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read from camera.")
            break

        cv2.imshow('frame', frame)
        cv2.imwrite(os.path.join(class_dir, f'{counter}.jpg'), frame)  # Save image
        counter += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'Q' to stop early
            print("Early exit during data collection.")
            break

    print(f"Completed collecting data for class {j}")

cap.release()
cv2.destroyAllWindows()
