#!/usr/bin/env python3
"""
Example usage of the ODrive python library to monitor and control ODrive devices
"""
from __future__ import print_function


import odrive
from odrive.enums import *
import time
import math
import Move

# motor disposition ====
#odrv0.axis0 = motor 2
#odrv0.axis1 =motor 3
#odrv1.axis0 = motor 4
#odrv1.axis1 =motor 1

# motor and encoder vars
cpr = 2048#512*4
radius=30 #mm
mm_to_count=(cpr)/(radius*2*math.pi)

# setpoint
tolerance=10 # encoder pulses

# Find a connected ODrive (this will block until you connect one)

seek1=False
seek2=False

while not (seek1 and seek2):

    print("finding an odrive...")
    odrv0 = odrive.find_any("usb","208D39854D4D")
    odrv1 = odrive.find_any("usb","207239854D4D")

    # motor 1 swapped by 2

    if  (odrv0.serial_number== 35790927514957) and not seek1:
        wheel1 = odrv0.axis0.controller
        encoder1=odrv0.axis0.encoder
        wheel1_config=odrv0.axis0.trap_traj.config

        wheel3 = odrv0.axis1.controller
        encoder3=odrv0.axis1.encoder
        wheel3_config=odrv0.axis1.trap_traj.config

        seek1=True
        print("find odrive1!")

    if  (odrv1.serial_number== 35674963397965) and not seek2:
        wheel4 = odrv1.axis0.controller
        encoder4=odrv1.axis0.encoder
        wheel4_config=odrv1.axis0.trap_traj.config

        wheel2 = odrv1.axis1.controller
        encoder2=odrv1.axis1.encoder
        wheel2_config=odrv1.axis1.trap_traj.config
        seek2 =True
        print("find odrive2!")

#configure parameters of wheels
wheel1_config.decel_limit=100000
wheel1_config.accel_limit=100000
wheel1_config.vel_limit=1000000


wheel2_config.decel_limit=100000
wheel2_config.accel_limit=100000
wheel2_config.vel_limit=1000000


wheel3_config.decel_limit=100000
wheel3_config.accel_limit=100000
wheel3_config.vel_limit=1000000


wheel4_config.decel_limit=100000
wheel4_config.accel_limit=100000
wheel4_config.vel_limit=1000000

print("config finished")



#=============================================================
#====================   main program  ========================
# ESPERAR TIRADOR!!!!!!!!!!!
'''
print("waiting tirador")
ser_us.write(serial.to_bytes([0XFA,0X10,0X10,0X20,0X00]))# preguntem si hi ha tirador
ser_us.read()
ser_us.read()
print("GO!")
'''
file = open("Coords_Groc.txt", "r")

dist_w1=0
dist_w2=0
dist_w3=0
dist_w4=0

for line in file:
            line=line.split()
            print("-------------------------------: ",line)
            distance=float(line[0])
            # Y_Coord=int(line[1])
            angulo=int(line[2])
            action=int(line[3])

            #all the moves are reversed
            wheel1_const=1*Move.Move(angulo,11)*Move.Move(angulo,1)*-1
            dist_w1+=distance*wheel1_const
            print("wheel1_const: ", wheel1_const)
            wheel1.move_to_pos(dist_w1*mm_to_count)

            wheel2_const=1*Move.Move(angulo,12)*Move.Move(angulo,2)*-1
            dist_w2+=distance*wheel2_const
            print("wheel2_const: ", wheel2_const)
            wheel2.move_to_pos(dist_w2*mm_to_count)


            wheel3_const=1*Move.Move(angulo,13)*Move.Move(angulo,3)*-1
            dist_w3+=distance*wheel3_const
            print("wheel3_const: ", wheel3_const)
            wheel3.move_to_pos(dist_w3*mm_to_count)

            wheel4_const=1*Move.Move(angulo,14)*Move.Move(angulo,4)*-1
            dist_w4+=distance*wheel4_const
            print("wheel4_const: ", wheel4_const)
            wheel4.move_to_pos(dist_w4*mm_to_count)


            print("wheel1: ",dist_w1*mm_to_count,"encoder: ",encoder1.pos_estimate)
            print("wheel2: ",dist_w2*mm_to_count)
            print("wheel3: ",dist_w3*mm_to_count)
            print("wheel4: ",dist_w4*mm_to_count)

            if wheel1_const==1:
                while encoder1.pos_estimate < dist_w1*mm_to_count-tolerance:
                    print("E1: ",encoder1.pos_estimate," ---> ",dist_w1*mm_to_count)
                    time.sleep(0.10)
                    if (odrv0.vbus_voltage <=14.8):#and (odrv1.vbus_voltage >=14.8):# security condition
                        exit()


            elif wheel1_const==0: #if wheel 1 not moves, 2 does
                if wheel2_const==1:
                    while encoder2.pos_estimate < dist_w2*mm_to_count-tolerance:
                        print("E2: ",encoder2.pos_estimate," ---> ",dist_w2*mm_to_count)
                        time.sleep(0.10)
                        if (odrv0.vbus_voltage <=14.8):#and (odrv1.vbus_voltage >=14.8):# security condition
                            exit()

                elif wheel2_const==-1:
                    while encoder2.pos_estimate > dist_w2*mm_to_count+tolerance:
                        print("E2: ",encoder2.pos_estimate," ---> ",dist_w2*mm_to_count)
                        time.sleep(0.10)
                        if (odrv0.vbus_voltage <=14.8):#and (odrv1.vbus_voltage >=14.8):# security condition
                            exit()

            elif wheel1_const==-1:
                while encoder1.pos_estimate > dist_w1*mm_to_count+tolerance:
                    print("E1: ",encoder1.pos_estimate," ---> ",dist_w1*mm_to_count)
                    time.sleep(0.10)
                    if (odrv0.vbus_voltage <=14.8):#and (odrv1.vbus_voltage >=14.8):# security condition
                        exit()


            print("========== NEXT MOVE ==========")

# Some more things you can try:

# Write to a read-only property:
#my_drive.vbus_voltage = 11.0  # fails with `AttributeError: can't set attribute`

# Assign an incompatible value:
#my_drive.motor0.pos_setpoint = "I like trains"  # fails with `ValueError: could not convert string to float`
for i in range(0,10):
    print("===========>>>>>>>>>>>>>>> VOLTAGE WARNING! <<<<<<<<<<<<<==============")
