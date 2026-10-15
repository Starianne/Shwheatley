import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP2)
led.direction = digitalio.Direction.OUTPUT

#led.value = True

# while True:
#     pass


# def longBlink():
#     led.value = not led.value
#     time.sleep(0.1)

# def shortBlink():
#     led.value = not led.value
#     time.sleep(0.05)


# while True:
#     for i in range(3):
#         shortBlink()
#     for i in range(3):
#         longBlink()
#     for i in range(3):
#         shortBlink()
#     time.sleep(1)

# while True:
#     led.value = not led.value
#     time.sleep(0.05)


while True:
    led.value= not led.value
    time.sleep(0.1)
    