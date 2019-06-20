
moves = [ ] 
def distotime(dis, moves):
    sp_r = 
    sp_l = 
    sp_d = 170
    sp_u = 135  #mm/s
    dt = 2

    
    for di in dis:
        if di[2] <= 50 :
            if di[0] == 0:
                moves = [ 'r', 'd', dt, 'd', dt, 's', (abs(di[1])-275)/sp_u, 'l', 'w', (2*di[2]+10)/sp_d, 'p', 'a', dt, 'a', dt, 's', (abs(di[1])-2*di[2]-280)/sp_d, 't']
            elif di[0]>0 and di[1]<0:
                moves = ['w', (abs(di[1]))/sp_u, 'a', dt, 's', (abs(di[0])-275)/sp_r, 'l', 'w', (2*di[2]+10)/sp_l, 'p', 'w', (abs(di[0])-2*di[2]-285)/sp_l,'d', dt, 's', abs(di[1])/sp_d, 't' ]
                if moves[4] < 0:
                    moves = ['r', 'd', dt, 'w', abs(di[0])/sp_r, 'd', dt, 's', (abs(di[1])-275)/sp_u, 'l', 'w' ,(2*di[2]+30)/sp_d, 'p', 'a', dt, 's', abs(di[0])/sp_l, 'a', dt, 's', (abs(di[0])-305-2*di[2])/sp_d, 't']
            elif di[1]>=0 and di[0]>0 :
                moves = ['w', 275/sp_u, 'a', dt, 's', abs(di[0])/sp_r, 'd', dt, 's', (abs(di[1])+2*di[2]+285)/sp_d, 'l', 'w', (2*di[2]+10)/sp_u, 'p', 's', 275/sp_d, 'd', dt, 's', abs(di[0])/sp_r, 'r', 'a', dt, 'p', 't' ]
            elif di[1]>=0 and di[0]<0:
                moves = ['w', 275/sp_u, 'd', dt, 's', abs(di[0])/sp_l, 'a', dt, 's', (abs(di[1])+2*di[2]+285)/sp_d, 'l', 'w', (2*di[2]+10)/sp_u, 'p', 's', 275/sp_d, 'a', dt, 's', abs(di[0])/sp_r, 'r', 'd', dt, 'p', 't' ]
            elif di[0]<0 and di[1]<0:
                moves = ['w', (abs(di[1]))/sp_u, 'd', dt, 's', (abs(di[0])-275)/sp_l, 'l', 'w', (2*di[2]+10)/sp_r, 'p', 'w', (abs(di[0])-2*di[2]-285)/sp_r,'a', dt, 's', abs(di[1])/sp_d, 't']
                if moves[4] < 0:
                    moves = ['r', 'a', 'w', abs(di[0])/sp_l, 'a', dt, 's', (abs(di[1])-275)/sp_u, 'l', 'w' ,(2*di[2]+30)/sp_d, 'p', 'd', dt, 's', abs(di[0])/sp_r, 'd', dt, 's', (abs(di[0])-285-2*di[2])/sp_d, 't']
                             
        elif 50<di[2]<=100:
            if di[0] == 0:
                moves = [ 'r', 'd', dt, 'w', 50/sp_r, 'd', dt, 's', (abs(di[1])-275)/sp_u, 'l', 'w', (2*di[2]+10)/sp_d, 'p', 'd', dt, 'w', 100/sp_l, 'a', dt, 's', (2*di[2]+10)/sp_u, 'l', 'w', (2*di[2]+10)/sp_d, 'p', 'a', dt, 'w', 50/sp_r, 'a', dt, 's', (abs(di[1])-280)/sp_d, 't']
            elif di[0]>0 and di[1]<0:
                moves = ['w', (abs(di[1])+50)/sp_u, 'a', dt, 's', (abs(di[0])-275)/sp_r, 'l', 'w', (2*di[2]+10)/sp_l, 'p', 'a', dt, 'w', 100/sp_d, 'd', dt, 's', (2*di[2]+10)/sp_r, 'l', 'w', (2*di[2]+10)/sp_l, 'p', 'w', (abs(di[0])-2*di[2]-285)/sp_l, 'd', dt, 's', abs(di[1])/sp_d, 't' ]
                if moves[4] < 0:
                    moves = ['r', 'd', dt, 'w', (abs(di[0])+50)/sp_l, 'd', dt, 's', (abs(di[1])-275)/sp_u, 'l', 'w' ,(2*di[2]+10)/sp_d, 'p', 'd', dt, 'w', 100/sp_r, 'a', dt, 's', (2*di[2]+10)/sp_u, 'l', 'w', (2*di[2]+10)/sp_d, 'p', 'd', dt, 'w', abs(di[0]-50)/sp_r, 'd', dt, 's', (abs(di[0])-285-2*di[2])/sp_d, 't' ]
            elif di[1]>=0 and di[0]>0 :
                moves = ['w', 405/sp_u, 'a', dt, 's', (abs(di[0])+50)/sp_r, 'd', dt, 's', (abs(di[1])+2*di[2]+415)/sp_d, 'l', 'w', (2*di[2]+10)/sp_u, 'p', 'd', dt, 's', 100/sp_l, 'a', dt, 's', (2*di[2]+10)/sp_d, 'l', 'w', (2*di[2]+10)/sp_u, 'p', 's', (275+di[2]-di[1])/sp_d, 'd', dt, 's', (abs(di[0])-50)/sp_l, 'r', 'a', dt, 'p', 't' ]
            elif di[1]>=0 and di[0]<0:
                moves = ['w', 405/sp_u, 'd', dt, 's', (abs(di[0])+50)/sp_l, 'a', dt, 's', (abs(di[1])+2*di[2]+415)/sp_d, 'l', 'w', (2*di[2]+10)/sp_u, 'p', 'a', dt, 's', 100/sp_r, 'd', dt, 's', (2*di[2]+10)/sp_d, 'l', 'w', (2*di[2]+10)/sp_u, 'p', 's', (275+di[2]-di[1])/sp_d, 'a', dt, 's', (abs(di[0])-50)/sp_l, 'r', 'd', dt, 'p', 't' ]
            elif di[0]<0 and di[1]<0:
                moves = ['w', (abs(di[1])+50)/sp_u, 'd', dt, 's', (abs(di[0])-275)/sp_l, 'l', 'w', (2*di[2]+10)/sp_r, 'p', 'd', dt, 'w', 100/sp_d, 'a', dt, 's', (2*di[2]+10)/sp_l, 'l', 'w', (2*di[2]+10)/sp_r, 'p', 'w', (abs(di[0])-2*di[2]-285)/sp_r, 'a', dt, 's', abs(di[1])/sp_d, 't' ]
                if moves[4] < 0:
                    moves = ['r', 'a', dt, 'w', (abs(di[0])+50)/sp_l, 'a', dt, 's', (abs(di[1])-275)/sp_u, 'l', 'w' ,(2*di[2]+10)/sp_d, 'p', 'a', dt, 'w', 100/sp_l, 'd', dt, 's', (2*di[2]+10)/sp_u, 'l', 'w', (2*di[2]+10)/sp_d, 'p', 'a', dt, 'w', abs(di[0]-50)/sp_r, 'a', dt, 's', (abs(di[0])-285-2*di[2])/sp_d, 't' ]
                             
        elif 100<di[2]:
            if di[0]>=0:
                i = (2*di[2])//100
                if (2*di[2])%100 == 0:
                    i = i-1
                y = (abs(di[1]) + (di[2] - 50)) / sp_u
                if (abs(di[0]) - 275) < di[2]:
                    x = (di[2] - abs(di[0]) +275)/sp_l
                    moves = [ 'w', y , 'a', dt, 'w', x, 's', 2*di[2]/sp_r, 'l', 'w', 2*di[2]/sp_l, 'p' ]
                    j = i
                    while i > 0 :
                        moves.append('d')
                        moves.append(dt)
                        moves.append('s')
                        moves.append(100/sp_d)
                        moves.append('a')
                        moves.append(dt)
                        moves.append('s')
                        moves.append((2*di[2]+5)/sp_r)
                        moves.append('l')
                        moves.append('w')
                        moves.append((2*di[2]+5)/sp_l)
                        moves.append('p')
                        i = i - 1
                    y = ((y*sp_u) - (j*100))/sp_d
                    moves.append('s')
                    moves.append(x*sp_l/sp_r)
                    moves.append('d')
                    moves.append(dt)
                    moves.append('s')
                    moves.append(y)
                elif (abs(di[0]) - 275) > di[2]:
                    x = (abs(di[0]) - di[2] - 275)/sp_r
                    moves = [ 'w', y , 'a', dt, 's', x + (2*di[2]/sp_r), 'l', 'w', 2*di[2]/sp_l, 'p' ]
                    j = i
                    while i > 0 :
                        moves.append('d')
                        moves.append(dt)
                        moves.append('s')
                        moves.append(100/sp_d)
                        moves.append('a')
                        moves.append(dt)
                        moves.append('s')
                        moves.append((2*di[2]+5)/sp_r)
                        moves.append('l')
                        moves.append('w')
                        moves.append((2*di[2]+5)/sp_l)
                        moves.append('p')
                        i = i - 1
                    y = ((y*sp_u) - (j*100))/sp_d
                    moves.append('w')
                    moves.append(x*sp_r/sp_l)
                    moves.append('d')
                    moves.append(dt)
                    moves.append('s')
                    moves.append(y)
                elif (abs(di[0]) - 275) == di[2]:
                    moves = [ 'w', y , 'a', dt, 's', 2*di[2]/sp_l, 'l', 'w', 2*di[2]/sp_r, 'p' ]
                    j = i
                    while i > 0 :
                        moves.append('d')
                        moves.append(dt)
                        moves.append('s')
                        moves.append(100/sp_d)
                        moves.append('a')
                        moves.append(dt)
                        moves.append('s')
                        moves.append(2*di[2]+5/sp_l)
                        moves.append('l')
                        moves.append('w')
                        moves.append(2*di[2]+5/sp_r)
                        moves.append('p')
                        i = i - 1
                    y = ((y*sp_u) - (j*100))/sp_d
                    moves.append('d')
                    moves.append(dt)
                    moves.append('s')
                    moves.append(y)
            elif di[0] < 0:
                i = (2*di[2])//100
                if (2*di[2])%100 == 0:
                    i = i-1
                y = (abs(di[1]) + (di[2] - 50)) / sp_u
                if (abs(di[0]) - 275) < di[2]:
                    x = (di[2] - abs(di[0]) +275)/sp_l
                    moves = [ 'w', y , 'd', dt, 'w', x, 's', 2*di[2]/sp_r, 'l', 'w', 2*di[2]/sp_l, 'p' ]
                    j = i
                    while i > 0 :
                        moves.append('d')
                        moves.append(dt)
                        moves.append('w')
                        moves.append(100/sp_d)
                        moves.append('a')
                        moves.append(dt)
                        moves.append('s')
                        moves.append(2*di[2]+5/sp_r)
                        moves.append('l')
                        moves.append('w')
                        moves.append(2*di[2]+5/sp_l)
                        moves.append('p')
                        i = i - 1
                    y = ((y*sp_u) - (j*100))/sp_d
                    moves.append('s')
                    moves.append(x*sp_l/sp_r)
                    moves.append('a')
                    moves.append(dt)
                    moves.append('s')
                    moves.append(y)
                elif (abs(di[0]) - 275) > di[2]:
                    x = (abs(di[0]) - di[2] - 275)/sp_r
                    moves = [ 'w', y , 'd', dt, 's', x + (2*di[2]/sp_r), 'l', 'w', 2*di[2]/sp_l, 'p' ]
                    j = i
                    while i > 0 :
                        moves.append('d')
                        moves.append(dt)
                        moves.append('w')
                        moves.append(100/sp_d)
                        moves.append('a')
                        moves.append(dt)
                        moves.append('s')
                        moves.append(2*di[2]+5/sp_r)
                        moves.append('l')
                        moves.append('w')
                        moves.append(2*di[2]+5/sp_l)
                        moves.append('p')
                        i = i - 1
                    y = ((y*sp_u) - (j*100))/sp_d
                    moves.append('w')
                    moves.append(x)
                    moves.append('a')
                    moves.append(dt)
                    moves.append('s')
                    moves.append(y)
                elif (abs(di[0]) - 275) == di[2]:
                    moves = [ 'w', y , 'd', dt, 's', 2*di[2]/sp_r, 'l', 'w', 2*di[2]/sp_l, 'p' ]
                    j = i
                    while i > 0 :
                        moves.append('d')
                        moves.append(dt)
                        moves.append('w')
                        moves.append(100/sp_d)
                        moves.append('a')
                        moves.append(dt)
                        moves.append('s')
                        moves.append(2*di[2]+5/sp_r)
                        moves.append('l')
                        moves.append('w')
                        moves.append(2*di[2]+5/sp_l)
                        moves.append('p')
                        i = i - 1
                    y = ((y*sp_u) - (j*100))/sp_d
                    moves.append('a')
                    moves.append(dt)
                    moves.append('s')
                    moves.append(y)
    moves.insert(0,'2')            
    return moves
            
    
    
    
