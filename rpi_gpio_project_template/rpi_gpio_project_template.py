""" A template for entry point class to be used with RPi.GPIO """
import atexit
import RPi.GPIO as GPIO

class Main:
    """ Main class program """

    def __init__(self):
        """ Insance fields definition """

    def _setup(self):
        """ Setup function (Will execute only one time) """
        atexit.register(self._clean)

    def _loop(self):
        """ Loop function (Will execute every tick) """
        while True:
            pass

    def _clean(self):
        """ Clean up function (Will execute when program exits) """
        GPIO.cleanup()

    def start(self):
        """ Entrypoint of the program """
        try:
            self._setup()
            self._loop()
        except (KeyboardInterrupt, SystemExit):
            self._clean()
        finally:
            self._clean()

def main():
    """
    Global function to initiate the module
    used for setup.py as an enttry point
    """
    Main().start()

if __name__ == "__main__":
    main()
