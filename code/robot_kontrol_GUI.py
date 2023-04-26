import tkinter as tk
import time
import serial



root = tk.Tk()
root.geometry("640x363")
root.title("Robot Kol Kontrol Programı v1.0(BETA)")
root.configure(bg='#ffffff')
ser = serial.Serial('/dev/cu.usbmodem14101', 9600) # /dev/cu.usbmodem14101 yerine kullandığınız portun ismini yazın




def set_servo_angle(servo, angle):
    # Servo açısını ayarlamak için kullanacağımız komut
    command = '{} {}\n'.format(servo, angle)
    # Komutu seri port aracılığıyla Arduino'ya gönderin
    ser.write(command.encode())
    # Arduino'dan cevap gelmesini bekleyin
    time.sleep(0.1)
    while ser.in_waiting > 0:
        response = ser.readline().decode().strip()
        print(response)



servo1 = 1
servo2 = 2
servo3 = 3
servo4 = 4

# Servo açılarını belirleyin
angle1 = 90
angle2 = 0
angle3 = 180
angle4 = 45
#servo açılarının bekleme modundaki halleri
angle1_SB = 0
angle2_SB = 0
angle3_SB = 0
angle4_SB = 0



def start():
    print("Robot Kol Başlatılıyor")
    ser.write(b'ON')
    
    

def stop():
    print("Robot Kol Kapatılıyor")
    ser.write(b'OFF')


def standby():
    print("Robot Standby Pozisyonuna Geçiyor")
    
    set_servo_angle(servo1, angle1_SB)
    set_servo_angle(servo2, angle2_SB)
    set_servo_angle(servo3, angle3_SB)
    set_servo_angle(servo4, angle4_SB)
    


def servo_check():
    
    set_servo_angle(servo1, angle1)
    set_servo_angle(servo2, angle2)
    set_servo_angle(servo3, angle3)
    set_servo_angle(servo4, angle4)
    
    print('2')

def exit():
    print("Sistem 5 Saniye İçinde Kapanacak")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    root.destroy()
    



yazi = tk.Label(text="Güç Kontolleri" )

yazi['font'] = "Verdana 15 bold"
yazi['fg'] = "#000000"
yazi['bg'] = "#ffffff"
yazi.place(x=235,y=80)

yazi2 = tk.Label(text="Robot Kontrolleri" )

yazi2['font'] = "Verdana 15 bold"
yazi2['fg'] = "#000000"
yazi2['bg'] = "#ffffff"
yazi2.place(x=235,y=165)

start = tk.Button(text="start", font="verdana 12 bold", command=start).place(x=200,y=128)
stop = tk.Button(text="stop", font="verdana 12 bold", command=stop).place(x=325,y=128)
standby = tk.Button(text="standby", font="verdana 12 bold", command=standby).place(x=325,y=200)
exit = tk.Button(text="exit", font="verdana 12 bold", command=exit).place(x=535,y=325)
servo_check = tk.Button(text="servo check", font="verdana 12 bold", command=servo_check).place(x=155,y=200)

root.mainloop()
