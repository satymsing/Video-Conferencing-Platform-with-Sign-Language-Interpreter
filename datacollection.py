import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 4
dataset_size = 100

# Use the correct camera index
cap = cv2.VideoCapture(0)

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print('Collecting data for class {}'.format(j))
    print('Ready? Press "Q" ! :)')

    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)

        # Check if frame dimensions are valid
        if frame is not None and frame.shape[0] > 0 and frame.shape[1] > 0:
            cv2.imwrite(os.path.join(class_dir, '{}.jpg'.format(counter)), frame)
            counter += 1

# Release the camera after collecting data for all classes
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
