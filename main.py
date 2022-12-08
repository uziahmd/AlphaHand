import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(maxHands=1)

timer = 0
stateResult = False
startGame = False
scores = [0, 0]  # [AI, Player]

import modi
# import time

def scissor(motor1, motor2):
    motor2.first_degree = 30
    motor1.second_degree = 40
    time.sleep(2)
    motor2.first_degree = 0
    motor1.second_degree = 0

def rock(motor1, motor2):
    motor2.first_degree = 30
    motor1.degree = 40, 30
    time.sleep(2)
    motor2.first_degree = 0
    motor1.degree = 0, 0

def paper(motor1, motor2):
    pass

# if __name__ == "__main__":
bundle = modi.MODI(1)
motor1 = bundle.motors[0]
motor2 = bundle.motors[1]
display = bundle.displays[0]

#     # inp = "rock"
#     # inp = "paper"
#     # inp = "scissor"

#     if inp=="scissor":
#         display.text = "scissor"
#         scissor(motor1, motor2)
#         time.sleep(1)
#         display.clear()
#     elif inp=="rock":
#         display.text = "rock"
#         rock(motor1, motor2)
#         time.sleep(1)
#         display.clear()
#     else:
#         display.text("paper")
#         paper(motor1, motor2)
#         time.sleep(1)
#         display.clear()


while True:
    imgBG = cv2.imread("Resources/BG.png")
    success, img = cap.read()

    imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
    imgScaled = imgScaled[:, 80:480]

    # Find Hands
    hands, img = detector.findHands(imgScaled)  # with draw

    if startGame:

        if stateResult is False:
            timer = time.time() - initialTime
            cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

            if timer > 3:
                stateResult = True
                timer = 0

                if hands:
                    playerMove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    print(fingers) # 1D array of size 5
                    if fingers == [0, 0, 0, 0, 0]:
                        playerMove = 1 # rock
                    if fingers == [1, 1, 1, 1, 1]:
                        playerMove = 2 # paper
                    if fingers == [0, 1, 1, 0, 0]:
                        playerMove = 3 # scisor

                    randomNumber = random.randint(1, 3)
                    
                    # bundle = modi.MODI(1)
                    # motor1 = bundle.motors[0]
                    # motor2 = bundle.motors[1]
                    # display = bundle.displays[0]

                    if randomNumber==3: #"scissor"
                        display.text = "scissor"
                        scissor(motor1, motor2)
                        time.sleep(3)
                        display.clear()
                    elif randomNumber==1: #"rock":
                        display.text = "rock"
                        rock(motor1, motor2)
                        time.sleep(3)
                        display.clear()
                    elif randomNumber==2: 
                        display.text="paper"
                        paper(motor1, motor2)
                        time.sleep(3)
                        display.clear()

                    imgAI = cv2.imread(f'Resources/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                    imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

                    # Player Wins
                    if (playerMove == 1 and randomNumber == 3) or \
                            (playerMove == 2 and randomNumber == 1) or \
                            (playerMove == 3 and randomNumber == 2):
                        scores[1] += 1

                    # AI Wins
                    if (playerMove == 3 and randomNumber == 1) or \
                            (playerMove == 1 and randomNumber == 2) or \
                            (playerMove == 2 and randomNumber == 3):
                        scores[0] += 1

    imgBG[234:654, 795:1195] = imgScaled

    if stateResult:
        imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

    cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

    # cv2.imshow("Image", img)
    cv2.imshow("BG", imgBG)
    # cv2.imshow("Scaled", imgScaled)

    key = cv2.waitKey(1)
    if key == ord('s'):
        startGame = True
        initialTime = time.time()
        stateResult = False