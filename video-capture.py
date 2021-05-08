import cv2
import imutils

# capture the video
video = cv2.VideoCapture(0)

while True:
    # reading the videofeed frame by frame
    frames = video.read()[1]
    
    # show the video frame
    cv2.imshow("video", frames)
    
    # close the window if key is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
       break
   
# once video is closed release it.   
firstImage.release()
cv2.destroyAllWindows()
