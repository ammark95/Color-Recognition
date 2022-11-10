import cv2
import time


cap = cv2.VideoCapture(0) #0 is an index for your webcam. if you have a second cam, input 1,2,etc.
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True: #the loop allows the code to be applied to a video
    _, frame = cap.read() #this single line grabs feed from a single frame in a single photo
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow("Frame", frame)
    height, width, _ = frame.shape
    cx = int(width / 2)
    cy = int(height / 2)
    
    #Establishes target pixel
    pixel_center = frame [cy, cx]
    print(pixel_center)

    hue_value = pixel_center[0]

    color = "Undefined"
    if hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 170:
        color = "VIOLET"
    else:
        color = "RED"

    pixel_center_bgr =frame [cy, cx]
    cv2.putText(frame, color, (10,50),2, 1, (255,255,255), 2)
    cv2.circle(frame, (cx,cy), 5, (255,0,0),3) #pixel color

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release
cv2.destroyAllWindows()


