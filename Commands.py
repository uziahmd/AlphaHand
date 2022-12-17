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
    time.sleep(2)
    motor2.first_degree = 0
    motor1.degree = 0, 0
