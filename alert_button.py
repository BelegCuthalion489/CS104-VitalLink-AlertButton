from dotenv import load_dotenv
import os
import time
import RPi.GPIO as GPIO
import requests
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

load_dotenv()
token = os.getenv("TELEGRAM_BOT_TOKEN")
print("Press the button")

button_pressed = False
while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        get_api = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={"chat_id": "8506760174", "text": "Someone pressed the alert button!"}
        )       
        button_pressed = True
    elif GPIO.input(7) == GPIO.LOW:
        button_pressed = False
    time.sleep(0.1)
