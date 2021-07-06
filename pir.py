import pyfirmata
import time


port='COM10'  #port number through which arduino is connected
board=pyfirmata.Arduino(port)  
time.sleep(2)
it=pyfirmata.util.Iterator(board)  # Start Iterator to avoid serial overflow
it.start()
f=open('soham.txt','w')   #create a file to save the information

def printf(message,pin):
    print(message,end=' ')
    print(time.ctime())
    f.write(message+' '+time.ctime())
    board.digital[pin].write(1) #eqivalent to "digitalWrite()" command of arduino
    time.sleep(1)
    board.digital[pin].write(0)
    time.sleep(1)

pin=board.get_pin('d:7:i') #define the pin type("Analog(a) or Digital(d)"),Pin number,Input(i) or Output(o)

                           #Pin no. 7 for PIR sensor
while True:
    value=pin.read()  #read the pin state
    
    if(value==1):     #if pin state is high
        
        printf("motion is detected",13)  # pin no.13 and 12 pin is for led
        
    else:
        printf("motion is not detected",12)
        d=0

board.exit()


        
    
    
