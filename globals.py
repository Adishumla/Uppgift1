import GPIO 

led1 = GPIO.OutputDevice(17) 
led2 = GPIO.OutputDevice(27) 
#led3 = GPIO.OutputDevice(22) 

button1 = GPIO.Button(23) 
#button2 = GPIO.Button(24) 
button1.enable_interrupt() 
#button1.enable_interrupt() 

deviceCollection = GPIO.OutputDeviceCollection() 
deviceCollection.add(led1) 
deviceCollection.add(led2) 
#deviceCollection.add(led3) 

fsm = GPIO.FSM(deviceCollection) 