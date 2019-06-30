import port2arduino as p2a
import time

def update_move(data, moves):
    sp_r = 167.0
    sp_l = 165.0
    sp_d = 170.0
    sp_u = 135.0  #mm/s
    dt = 2.0
    moves = ['m', 3, 'p', 3, 'w', float(abs(data[0][1])/sp_u), 't', 2, 'a', dt, 't', 2, 's', float(abs(data[0][0])/sp_r), 't', 2, 'l', 3, 'w', 
             float(abs(data[0][0])/sp_r), 't', 2, 'd', dt, 't', 2, 's', float(abs(data[0][1])/sp_d), 't']
    print(moves)
    time.sleep(5)
    p2a.data_send(moves)
