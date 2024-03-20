import time
from pymavlink import mavutil

master = mavutil.mavlink_connection('COM4', baud=57600)

master.wait_heartbeat()

while True:
    try:
        msg = master.recv_match(type='ATTITUDE', blocking=True)
        
        roll = msg.roll
        pitch = msg.pitch
        yaw = msg.yaw
        
        print("Roll: {0}, Pitch: {1}, Yaw: {2}".format(roll, pitch, yaw))
        
        time.sleep(0.1)
        
    except KeyboardInterrupt:
        print("exit program...")
        break
