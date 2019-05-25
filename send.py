import serial
ser = serial.Serial("/dev/ttyS0", 9600)


def left(x):
    for j in range(x):
        ser.write(b'\x02OCL\x03')
        sx = ser.read(5)

def right(x):

    for j in range(x):
        ser.write(b'\x02OCR\x03')
        sx = ser.read(5)

def up(x):
    for j in range(x):
        ser.write(b'\x02OCU\x03')
        sx = ser.read(5)

def down(x):
    for j in range(x):
        ser.write(b'\x02OCD\x03')
        sx = ser.read(5)

def enter():
    ser.write(b'\x02OEN\x03')
    sx = ser.read(5)

def menu():
    ser.write(b'\x02OMN\x03')
    sx = ser.read(5)


def OK():
    
    up(2)
    enter()
    enter()
    enter()
    down(2)
    left(1)

    print('Enter')

def number(x):

    right(1)
    down(4)
    right(x - 1)
    enter()
    left(x)
    up(4)
    left(1 - 1)
menu()
menu()
left(1)
print('Anchored on Delete')

for j in range(1, 10):
    for k in range(1, 10):
        for l in range(1, 10):
            for m in range(1, 10):
                z = 1000 * j + 100 * k + 10 * l + m;

                if( z > 2400 ):
                    print(z)            
                    number(j)
                    number(k)
                    number(l)
                    number(m)
                    OK()
                    enter()
                    enter()
                    enter()
                    enter()
