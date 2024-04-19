
import time
# Import mavutil
from pymavlink import mavutil

port = 'COM4'  # Seri portunu uygun şekilde değiştirin
baud = 57600  # Baud oranını uygun şekilde değiştirin

# MAVLink bağlantısını oluştur
master = mavutil.mavlink_connection(port, baud=baud)
# Wait a heartbeat before sending commands
master.wait_heartbeat()

def request_message_interval(master, message_input: str, frequency_hz: float):
    message_name = "MAVLINK_MSG_ID_" + message_input
    message_id = getattr(mavutil.mavlink, message_name)
    master.mav.command_long_send(
        master.target_system, master.target_component,
        mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL, 0,
        message_id,
        1e6 / frequency_hz,
        0,
        0, 0, 0, 0)
    print("Requested the message successfully.")

def get_requested_data(master, message_name: str, dict_key: str, value_unit: str, save_name: str):
    try:
        message_index = 0
        dict1 = master.recv_match(type= message_name, blocking=True, timeout=0.1).to_dict()
        dict_value = dict1[dict_key]
        toWrite = "Message_Index, " + message_index + " :" + str(dict_value) + value_unit
        with open(save_name, 'a') as file:
            file.write(toWrite)
            file.write('\n')  
            message_index += 1
    except:
        pass
    
request_message_interval(master, "VFR_HUD", 1)
while True:
    try:
        get_requested_data(master, "VFR_HUD", 'alt', "m", save_name)
    except:
        pass