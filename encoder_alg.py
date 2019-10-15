import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BOARD)

ENCODER = 4
lasttime = 0


try:
    def callback_up(channel):
        print(time.ctime())
        threading.Timer(.004, callback_up).start()
        global lasttime
        if lasttime == 0:
            lasttime = time.time()
        else:
            now = time.time()
            gap = now-lasttime
            print(gap)
            lasttime = now

        GPIO.add_event_detect(ENCODER, GPIO.RISING, callback=callback_up)
        while 1:
            time.sleep(10)

        callback_up()

except KeyboardInterrupt:
    GPIO.cleanup()


finally:
    GPIO.cleanup()
