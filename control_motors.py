from pymavlink import mavutil
import time

# MAVLink bağlantısı kur
master = mavutil.mavlink_connection('COM4', baud=57600)  # Raspberry Pi'deki seri portuna göre ayarlayın
print(type(master))

print(type(master.mav))
print(type(master.mav.manual_control_send))


# İleri veya geri hareket için kullanılacak değer (örneğin, 1500 motor durumu, 1700 tam hız ileri, 1300 tam hız geri)
throttle_forward = 1700  # İleri hareket için gaz değeri
throttle_reverse = 1300  # Geri hareket için gaz değeri

# Ana döngü
try:
        # Pixhawk'a gönderilecek mesajı oluştur
    msg = master.recv_match(type='HEARTBEAT', blocking=True)
    print("Heartbeat alındı.")

    while True:
        # İleri hareket komutu gönder
        master.mav.manual_control_send(master.target_system, throttle_forward, 0, 0, 0, 0)
        # Pixhawk'tan gelen bilgileri işle
        # Bu örnekte sadece HEARTBEAT mesajını bekliyoruz, diğer mesajlar da işlenebilir
        
        # Örneğin, motor komutu göndermek için:
        # master.mav.manual_control_send(master.target_system, 100, 0, 0, 0, 0)
        
        # veya diğer MAVLink mesajlarını kullanarak işlem yapabilirsiniz

        # 1 saniye bekle
        time.sleep(1)

        master.mav.manual_control_send(master.target_system, throttle_reverse, 0, 0, 0, 0)
        time.sleep(1)


except KeyboardInterrupt:
    print("Kesme alındı, program sonlandırılıyor...")

finally:
    master.close()  # Bağlantıyı kapat
