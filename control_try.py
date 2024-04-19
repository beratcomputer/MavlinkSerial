from pymavlink import mavutil
import time

# Seri bağlantı portu ve baud oranı
port = 'COM4'  # Seri portunu uygun şekilde değiştirin
baud = 57600  # Baud oranını uygun şekilde değiştirin

# MAVLink bağlantısını oluştur
master = mavutil.mavlink_connection(port, baud=baud)
master.set_mode_manual()

master.mav.command_long_send(master.target_system,master.target_component, mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM , 0, 1, 0, 0, 0, 0, 0,0)

# Sonsuz döngüde veri al
while True:
    for i in range (0, 1000,300):
        print(master.wait_heartbeat())
        master.mav.manual_control_send(master.target_system, x=0, y=i, z=0, r=0, buttons=0)
        print(i)

