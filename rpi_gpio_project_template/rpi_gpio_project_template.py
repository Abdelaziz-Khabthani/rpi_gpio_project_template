""" A template for entry point class to be used with RPi.GPIO """
import atexit
import time
import RPi.GPIO as GPIO


class RpiGpioProjectTemplate:
    """ Main class program """

    def __init__(self, init_delay = 0, loop_delay = 0):
        """ Insance fields definition """
        self._init_delay = init_delay
        self._loop_delay = loop_delay
        time.sleep(self._init_delay)

    def _setup(self):
        """ Setup function (Will execute only one time) """
        atexit.register(self._clean)

    def _loop(self):
        """ Loop function (Will execute every tick) """

    def _clean(self):
        """ Clean up function (Will execute when program exits) """
        GPIO.cleanup()

    def start(self):
        """ Entrypoint of the program """
        try:
            self._setup()
            time.sleep(self._init_delay)
            while True:
                self._loop()
                time.sleep(self._loop_delay)
        except (KeyboardInterrupt, SystemExit):
            self._clean()
        finally:
            self._clean()


def main():
    """ Global function to initiate the module (used for setup.py as an enttry point) """
    RpiGpioProjectTemplate(init_delay=1, loop_delay=0.025).start()


if __name__ == "__main__":
    main()
