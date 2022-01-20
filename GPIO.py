import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def delay(delay_time):
    import time
    time.sleep(float(delay_time) / 1000)
    return

class OutputDevice:

    def __init__(self, PIN):
        self.__PIN = PIN
        self.__enabled = False
        GPIO.setup(self.__PIN, GPIO.OUT)
        return

    def on(self):
        GPIO.output(self.__PIN, GPIO.HIGH)
        self.__enabled = True
        return

    def off(self):
        GPIO.output(self.__PIN, GPIO.LOW)
        self.__enabled = False
        return 

    def toggle(self):
        if self.__enabled: self.off()
        else: self.off()
        return

class OutputDeviceCollection: 

    def __init__(self):
        self.__devices = []
        self.__number_of_devices = 0
        return

    def add(self, device):
        self.__devices.append(device)
        self.__number_of_devices += 1
        return

    def clear(self):
        self.__devices.clear()
        self.__number_of_devices = 0
        return

    def on(self):
        for i in range(0, self.__number_of_devices, 1):
            device = self.__devices[i]
            device.on()
        return

    def off(self):
        for i in range(0, self.__number_of_devices, 1):
            device = self.__devices[i]
            device.off()
        return


    def blink(self, delay_time):
        for i in range(0, self.__number_of_devices, 1):
            self.off()
            device = self.__devices[i]
            device.on()
            delay(delay_time)
        return

class Button: # Frågas efter

    def __init__(self, PIN):
        self.__PIN = PIN
        GPIO.setup(self.__PIN, GPIO.IN)
        return

    def is_pressed(self):
        return GPIO.input(self.__PIN)

    def enable_interrupt(self, callback_routine):
        
        GPIO.add_event_detect(self.__PIN, GPIO.RISING, callback = callback_routine, bouncetime = 200)
        return

    def disable_interrupt(self):
        GPIO.remove_event_detect(self.__PIN)
        return

class State:

    def __init__(self, min, max):
        self.__min = min
        self.__max = max
        self.__state = self.__min
        return

    def next(self):
        self.__state += 1
        if self.__state > self.__max:
            self.__state = self.__min
        return  

    def previous(self):
        self.__state -= 1
        if self.__state < self.__min:
            self.__state = self.__max
        return
        
    def reset(self):
        self.__state = self.__min
        return

    def current(self):
        return self.__state


class FSM: # Frågas efter 

    def __init__(self, device):
        import const
        self.__state = State(const.OFF, const.ON)
        self.__slow_delay = const.SLOW_DELAY
        self.__medium_delay = const.MEDIUM_DELAY
        self.__fast_delay = const.FAST_DELAY
        self.__device = device
        return

    def next(self):
        self.__state.next()
        self.run()
        return

    def previous(self):
        self.__state.previous()
        self.run()
        return

    def reset(self):
        self.__state.reset() 
        self.__device.off()
        return

    def run(self):
        
        import const
        state = self.__state.current()
        if state == const.OFF: 
            self.__device.off()
        elif state == const.SLOW: 
            self.__device.blink(self.__slow_delay)
        elif state == const.MEDIUM:
            self.__device.blink(self.__medium_delay)
        elif state == const.FAST: 
            self.__device.blink(self.__fast_delay)
        elif state == const.ON: 
            self.__device.on()
        else: 
            self.reset()
        return