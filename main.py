from machine import Pin
from neopixel import NeoPixel
from time import sleep

pin = Pin(2, Pin.OUT)
np = NeoPixel(pin, 48)

index = 0
flag = ()

while True:
    print('Flag with index {}'.format(str(index)))
    with open('data.txt') as datafh:
        for num, line in enumerate(datafh):
            if num == index:
                flag = eval(line)
                index += 1
                break
        else:
            index = 0
    print('Flag data:')
    print(flag)
    for x in range(48):
        np[x] = flag[x]
    np.write()
    sleep(10)
