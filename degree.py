import modi
import time

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

if __name__ == "__main__":
    bundle = modi.MODI(1)
    motor1 = bundle.motors[0]
    motor2 = bundle.motors[1]
    display = bundle.displays[0]

    # inp = "rock"
    # inp = "paper"
    # inp = "scissor"

    if inp=="scissor":
        display.text = "scissor"
        scissor(motor1, motor2)
        time.sleep(1)
        display.clear()
    elif inp=="rock":
        display.text = "rock"
        rock(motor1, motor2)
        time.sleep(1)
        display.clear()
    else:
        display.text("paper")
        paper(motor1, motor2)
        time.sleep(1)
        display.clear()
