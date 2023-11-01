import time
import random
import board
import digitalio

led = digitalio.DigitalInOut(board.GP13)
led.direction = digitalio.Direction.OUTPUT
button_one = digitalio.DigitalInOut(board.GP14)
button_one.switch_to_input(pull=digitalio.Pull.DOWN)
button_two = digitalio.DigitalInOut(board.GP16)
button_two.switch_to_input(pull=digitalio.Pull.DOWN)

time.sleep(random.randint(1,5))
led.value = True
timer_start = time.monotonic()
while True:
    if button_one.value & button_two.value:
        reaction_time = (time.monotonic() - timer_start) * 1000
        print("red and green tied, your reaction time was", reaction_time, "ms")
        led.value = False
        break
    if button_one.value:
        reaction_time = (time.monotonic() - timer_start) * 1000  # Convert to ms
        print("red wins, your reaction time was", reaction_time, "ms")
        led.value = False
        break
    if button_two.value:
        reaction_time = (time.monotonic() - timer_start) * 1000  # Convert to ms
        print("green wins, your reaction time was", reaction_time, "ms")
        led.value = False
        break
