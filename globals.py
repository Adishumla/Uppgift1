import GPIO 
import interrupts

led1 = GPIO.OutputDevice(17) 
led2 = GPIO.OutputDevice(27) 
#led3 = GPIO.OutputDevice(22) 

button1 = GPIO.Button(23) 
button2 = GPIO.Button(24) 
button1.enable_interrupt(interrupts.button1_pressed) 
button2.enable_interrupt(interrupts.button2_pressed) 

deviceCollection = GPIO.OutputDeviceCollection() 
deviceCollection.add(led1) 
deviceCollection.add(led2) 
#deviceCollection.add(led3) 

fsm = GPIO.FSM(deviceCollection) 
