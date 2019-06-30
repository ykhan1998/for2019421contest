import serial
import time
import json
def data_send(moves):
    moves = ['w', 2, 't']
    moves = ['m', 3, 'p', 3, 'w', 4.155, 't', 2, 'a', 1.587, 't', 2, 's', 1.6, 't', 2, 'l', 3, 'w', 1.6, 't', 2, 'p', 2, 'd', 1.625, 't', 2, 's', 2.545, 't']
    s=serial.Serial( '/dev/rfcomm0', 9600 )
    print('Moves sending......')
    for move in moves:
        if type(move) is float:
            time.sleep(move)
        elif type(move) is int:
            time.sleep(move)
        elif move == 't':
            ob = str(move)
            mb = ob.encode(encoding="utf-8")  
            s.write(mb)
        else :
            ob = str(move)
            mb = ob.encode(encoding="utf-8")  
            s.write(mb)
    print('Finished')
