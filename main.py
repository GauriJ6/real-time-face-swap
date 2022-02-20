import cv2
from swap import swap_images
from utils import landmark_detection, detect_face, readPoints

if __name__ == '__main__' :
    # Read images

    cap = cv2.VideoCapture(0)

    while(True):
    # Capture frame-by-frame
        ret, img = cap.read()
        gray, rects = detect_face(img)
        if len(rects) == 1:
            points1, _ = landmark_detection(gray, rects)
            filename2 = 'donald_trump.jpg'
            img2 = cv2.imread(filename2);
            
points2 = readPoints(filename2+'.txt')

            output = swap_images(img2, img, points2, points1)
            cv2.imshow("Face Swapped", output)
        elif len(rects) == 2:
            points1, points2 = landmark_detection(gray, rects)
            output = swap_images(img, img, points2, points1)
            output = swap_images(img, output, points1, points2)
            cv2.imshow("Face Swapped", output)
        else:
            cv2.imshow("Face Swapped", img)

        if cv2.waitKey(1) &
if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
