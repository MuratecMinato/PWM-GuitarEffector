import machine
import time
from machine import PWM

# GP16をPWMに使うための設定
Led  = PWM(machine.Pin(15, machine.Pin.OUT))

Led.freq(261)	#Cド
time.sleep(2)

Led.duty_u16(52429)
time.sleep(2)

Led.freq(293)	#Dレ
time.sleep(2)

Led.freq(329)	#E
time.sleep(2)

Led.freq(349)	#F
time.sleep(2)

Led.freq(392)	#G
time.sleep(2)

Led.freq(440)	#A
time.sleep(2)

Led.freq(494)	#B
time.sleep(2)

Led.freq(523)	#C
time.sleep(2)

Led.duty_u16(0)
time.sleep(2)
