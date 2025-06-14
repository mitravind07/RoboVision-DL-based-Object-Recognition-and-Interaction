from pyfirmata import Arduino, SERVO
from time import sleep
import msvcrt

board = Arduino('COM10')

pin_13=board.digital[13] # base
pin_11=board.digital[11] # shoulder
pin_9 = board.digital[9] # elbow
pin_7 = board.digital[7] # gripper

pin_13.mode=SERVO
pin_11.mode=SERVO
pin_9.mode=SERVO
pin_7.mode=SERVO

i=76  # base
j=88 # shoulder
k=133 # elbow 
l=166 # gripper
m=0

pin_13.write(i)
pin_11.write(j)
pin_9.write(k)
pin_7.write(l)

def get_key_pressed():

    return msvcrt.getch().decode('utf-8')

while True:
    key = get_key_pressed()
    if key == 'a':
        print('a pressed : ',i)
        i += 1
        if i>=145:
            i=145
            continue
        pin_13.write(i)
        sleep(0.01)
    if key == 'd':
        print('d pressed : ',i)
        i -= 1
        if i<=27:
            i=27
            continue
        pin_13.write(i)
        sleep(0.01)
    if key == 's':
        print('s pressed : ',j)
        j -= 1
        if j<=80:
            j=80
            continue
        pin_11.write(j)
        sleep(0.01)    
    if key == 'w':
        print('w pressed : ',j)
        j += 1
        if j>=165:
            j=165
            continue
        pin_11.write(j)
        sleep(0.01)
    if key == '2':
        print('down pressed : ',k)
        k -= 1
        if k<=80 :
            k=80
            continue
        pin_9.write(k)
        sleep(0.01)
    if key == '8':
        print('up pressed : ',k)
        k += 1
        if k>=178:
            k=178
            continue
        pin_9.write(k)
        sleep(0.01)
    
    if key == ' ':
        m+=1
        print('space pressed')

        if m==1:
            for l in range (150,168,1):
                pin_7.write(l)
                sleep(0.02)

        if m==2:
            m=0
            for l in range (167,150,-1):
                pin_7.write(l)
                sleep(0.02)
    #if key == 'o':
        