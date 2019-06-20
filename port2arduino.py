import serial
import time
import json

'''with open('move.json') as file_obj:
    moves = json.load(file_obj)'''
moves = [ 'w', 2, 't']
s=serial.Serial( '/dev/rfcomm9', 9600 )
print('Moves sending......')
for move in moves:
    if type(move) is int:
        time.sleep(move)
    elif move == 't':
        ob = str(move)
        mb = ob.encode(encoding="utf-8")  
        s.write(mb)
        time.sleep(3)
    else :
        ob = str(move)
        mb = ob.encode(encoding="utf-8")  
        s.write(mb)
    print(move)
print('Finished')
'''ex = '<ctrl+z>'
exi = ex.encode(encoding="utf-8")    
s.write(exi)
print('Sending finished, total time : ' + str((len(moves)+1)))'''
