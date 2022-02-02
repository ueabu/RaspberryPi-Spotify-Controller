import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from SpotifyActions import *
import signal
import time

reader = SimpleMFRC522()

def startListening():
    try:
        while True:
            print('-------------------------------------')
            print("Listening .....")
            id, text = reader.read()
            print(id)
            play(id)
            print('-------------------------------------')
    except KeyboardInterrupt:
        GPIO.cleanup()
        raise
    except Exception:
        GPIO.cleanup()
        raise


def main():
    startListening()

if __name__ == "__main__":
    main()