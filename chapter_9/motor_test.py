#!/usr/bin/python3

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
from time import sleep


if __name__ == "__main__":
  motor_driver = AdaFruit_MotorHAT(addr=0x60)

  left_motor = motor_driver.getMotor(1)
  right_motor = motor_driver.getMotor(2)

  left_motor.setSpeed(255)
  right_motor.setSpeed(255)

  left_motor.run(Adafruit_MotorHAT.FORWARD)
  right_motor.run(Adafruit_MotorHAT.FORWARD)

  left_motor.run(Adafruit_MotorHAT.RELEASE)
  right_motor.run(Adafruit_MotorHAT.RELEASE)

  sleep(10)

  left_motor.setSpeed(200)
  right_motor.setSpeed(200)

  left_motor.run(Adafruit_MotorHAT.FORWARD)
  right_motor.run(Adafruit_MotorHAT.FORWARD)

  sleep(10)

  left_motor.run(Adafruit_MotorHAT.RELEASE)
  right_motor.run(Adafruit_MotorHAT.RELEASE)









