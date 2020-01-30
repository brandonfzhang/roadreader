from picar import front_wheels
from picar import back_wheels
from picar import ADC
import time
import picar

##picar.setup()

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')

gate_value = 30		# less then the normal, will act
forward_speed = 90
bw.speed = forward_speed

fw.turn(70)
bw.forward()
bw.backward()
fw.turn_straight()
fw.stop()
bw.stop()
