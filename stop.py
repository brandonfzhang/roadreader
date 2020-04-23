from picar import front_wheels
from picar import back_wheels
from picar import ADC
import picar

picar.setup()

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')

bw.stop()