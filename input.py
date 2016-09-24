# Reading a button press from your keyboard, don't worry about this too much!
import sys
import tty
import termios

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return ord(c3) - 65  # 0=Up, 1=Down, 2=Right, 3=Left arrows

# End of the functions that read your keyboard
try:
    while True:
        keyp = readkey()
        if keyp == 'w' or keyp == UP:
            print('Forward')
        elif keyp == 's' or keyp == DOWN:
            print('Backward')
        elif keyp == 'd' or keyp == RIGHT:
            print('Spin Right')
        elif keyp == 'a' or keyp == LEFT:
            print('Spin Left')
        else:
            print(keyp)

# When you want to exit - press ctrl+c and it will generate a keyboard interrupt - this is handled nicely here!
except KeyboardInterrupt:
    exit(0)
