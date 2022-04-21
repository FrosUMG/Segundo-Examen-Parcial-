import pyfirmata
import time

board = pyfirmata.Arduino('COM11')

it = pyfirmata.util.Iterator(board)
it.start()

board.digital[4].mode = pyfirmata.INPUT

while True:
    sw = board.digital[4].read()
    if sw is True:
        board.digital[12].write(1)
        time.sleep(5)
    else:
        board.digital[12].write(0)
    time.sleep(0.1)
