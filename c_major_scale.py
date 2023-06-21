import machine
import time
from machine import PWM

# GP16をPWMに使うための設定
pwm = PWM(machine.Pin(15, machine.Pin.OUT))
pwm.duty_u16(52429)
time.sleep(0.5)

pwm.freq(261)	#Cド
time.sleep(0.5)
print("C")

pwm.freq(293)	#Dレ
time.sleep(0.5)
print("D")

pwm.freq(329)	#E
time.sleep(0.5)
print("E")

pwm.freq(349)	#F
time.sleep(0.5)
print("F")

pwm.freq(392)	#G
time.sleep(0.5)
print("G")

pwm.freq(440)	#A
time.sleep(0.5)
print("A")

pwm.freq(494)	#B
time.sleep(0.5)
print("B")

pwm.freq(523)	#C
time.sleep(0.5)
print("C")

pwm.duty_u16(0)
time.sleep(0.5)