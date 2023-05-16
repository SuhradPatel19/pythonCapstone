import cv2
import mediapipe as mp
from pynput.keyboard import Key,Controller
import pyautogui

myKeyboard=Controller()

state=None

video=cv2.VideoCapture(0)
width=int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width,height)

myHands=mp.solutions.hands
myDrawing=mp.solutions.drawing_utils

handObject=myHands.Hands(min_detection_confidence=0.75,min_tracking_confidence=0.75)
print("hand object",handObject)

def countFingers(lst,myImage):
    global state
    count=0

    thresh=(lst.landmark[0].y*100-lst.landmark[9].y*100)/2
    # print(thresh)

    if(lst.landmark[5].y*100-lst.landmark[8].y*100)>thresh:
        count+=1
    if(lst.landmark[9].y*100-lst.landmark[12].y*100)>thresh:
        count+=1
    if(lst.landmark[13].y*100-lst.landmark[16].y*100)>thresh:
        count+=1
    if(lst.landmark[17].y*100-lst.landmark[20].y*100)>thresh:
        count+=1
    # if(lst.landmark[5].x*100-lst.landmark[4].x*100)>6:
    #     count+=1

    totalFingers=count

    if totalFingers ==4:
        state="play"
    if totalFingers ==0 and state=="play":
        state="pause"
        myKeyboard.press(Key.space)

    indexX=lst.landmark[8].x*width
    if totalFingers ==1:
        if indexX <width-400:
            state="forward"
            myKeyboard.press(Key.right)
    if totalFingers ==1:
        if indexX >width-100:
            state="backwards"
            myKeyboard.press(Key.left)

    indexY=lst.landmark[8].y*height

    if totalFingers==2:
        if indexY<height-250:
            print("Increasing Volume")
            pyautogui.press("volumeup")
        if indexY>height-250:
            print("Decreasing Volume")
            pyautogui.press("volumedown")

    return totalFingers
    
    

while True:
    dummy,frame=video.read()
    flipImage=cv2.flip(frame,1)

    result=handObject.process(cv2.cvtColor(flipImage,cv2.COLOR_BGR2RGB))
    # print(result)

    if result.multi_hand_landmarks:
        hand_keypoints=result.multi_hand_landmarks[0]
        # print(hand_keypoints)
        myDrawing.draw_landmarks(flipImage,hand_keypoints,myHands.HAND_CONNECTIONS)

        myCount=countFingers(hand_keypoints,flipImage)
        cv2.putText(flipImage,"Finger: "+str(myCount),(100,100),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,0))
        cv2.putText(flipImage,"State: "+str(state),(250,50),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,0))
    cv2.imshow("window",flipImage)
    key=cv2.waitKey(1 )

    if key==27:
        break
video.release()
cv2.destroyAllWindows 
