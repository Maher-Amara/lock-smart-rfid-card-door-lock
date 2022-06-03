import time
from keypad import keypad
from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
GPIO.setwarnings(False)

lcd = CharLCD(cols=16,rows=2,pin_rs=37, pin_e=35, pins_data=[33,31,29,40])
p=GPIO.PWM(13,20)
kp=keypad(columnCount = 3)
p.start(0)
code=[1,2,3,4]
while True :
    #lcd.write_string(u"code:" + str(list))
    lcd.write_string(u"Write the code")
    time.sleep(10)
    lcd.close(clear=True)
    list=[]
    GPIO.output(13,False)
    #lcd.write_string(u"write code")
    for i in range(len(code)) :
        digit = None
        while digit == None :
            digit=kp.getKey()
        list.append(digit)
        #lcd.close(clear=True)
        time.sleep(0.4)
        print(list)
        if len(list) == 4 :
            if list == code :
                #lcd.close(clear=True)
                p.ChangeDutyCycle(2.0)
                print("Door open")
                #lcd.write_string(u'Door open')
                time.sleep(5)
                #lcd.close(clear=True)
                p.ChangeDutyCycle(6.0)
                print("Door closed")
                #lcd.write_string(u'Door closed')
                #time.sleep(5)
                #lcd.close(clear=True)
                GPIO.output(13,True)
            else :
                print("Echec, code incorrect!")
                #lcd.write_string(u'Code incorrect!')
                #time.sleep(5)
                #lcd.close(clear=True)
                p.ChangeDutyCycle(6.0)
                GPIO.output(13,False)