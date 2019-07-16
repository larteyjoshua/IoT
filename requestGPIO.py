from gpiozero import Button
from signal import pause
import requests


button = Button(17)

def process():
    r = requests.get("https://maker.ifttt.com/trigger/joshua/with/key/nysGdnaf_1mFwgoEea7kvE-UFY68Bx2QDYPtznNyCtb")
    print ("Request Sent successfully")



print("Press the button to send request")
button.when_pressed = process

pause()
process()
