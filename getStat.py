from pymavlink import mavutil

# Seri bağlantı portu ve baud oranı
port = 'COM4'  # Seri portunu uygun şekilde değiştirin
baud = 57600  # Baud oranını uygun şekilde değiştirin

# MAVLink bağlantısını oluştur
master = mavutil.mavlink_connection(port, baud=baud)


message = master.recv_match()
# Sonsuz döngüde veri al
while True:

    try:
        # Bir sonraki MAVLink mesajını al
        message = master.recv_match()

        # Eğer mesaj varsa, yazdır
        if message:
            print(message)

    except KeyboardInterrupt:
        # Programı sonlandır
        break
