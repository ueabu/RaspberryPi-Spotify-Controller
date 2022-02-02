import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from SpotifyActions import *
import signal
import time

reader = SimpleMFRC522()

def startListening():
    try:
        while True:
            print("Hold a tag near the reader")
            id, text = reader.read()
            print("ID: %s\nText: %s" % (id,text))
            play(id)
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