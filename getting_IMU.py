import time
from pymavlink import mavutil

master = mavutil.mavlink_connection('COM4', baud=57600)
#print(master)
#print(type(master))
master.wait_heartbeat()
i = 0
msg = master.recv_match(type='ATTITUDE', blocking=True)
#print(msg)
#print(type(msg))

while True:
    try:
        roll = msg.roll
        pitch = msg.pitch
        yaw = msg.yaw
        
        print("Roll: {0}, Pitch: {1}, Yaw: {2}".format(roll, pitch, yaw))
        msg = master.recv_match(type='ATTITUDE', blocking=True)
        i+=1
        
    except KeyboardInterrupt:
        print("exit program...")
        break
