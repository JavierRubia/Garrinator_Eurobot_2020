


#def Move (angulo, M1, M2, M3, M4, M2p, M3p, M4p, M1p):
def Move (angulo,M):
   
    
    M1=1
    M2=1
    M3=5
    M4=1

    M1p = 1
    M2p = 1
    M3p = 1
    M4p = 1
    
    if angulo == 0:
        switch={
            1:-1, #M1
            2:-1, #M2
            3:1,  #M3
            4:1,  #M4

            11:1, #MP1
            12:1, #MP2
            13:1, #MP3
            14:1  #MP4
            }
        
        
    elif angulo == 45:
        switch={
            1: -1,
            4: 1,

            12: 0,
            13: 0
            }

    elif angulo == 90:
        switch={
            1: -1,
            2: 1,
            3: -1,
            4: 1
            }
        
    elif angulo == 135:
        switch={
            2: 1,
            3: -1,
            11: 0,
            14: 0
            }

    elif angulo == 180:
        switch={
            1: 1,
            2: 1,
            3: -1,
            4: -1
            }

    elif angulo == 225:
        switch={
            1: 1,
            4: -1,
            12: 0,
            13: 0
            }

    elif angulo == 270:
        switch={
            1: 1,
            2: -1,
            3: 1,
            4: -1
            }   

    elif angulo == 315:
        switch={
            2: -1,
            3: 1,
            11: 0,
            14: 0
            }

    elif angulo == 370:
        switch={
            1: 1,
            2: 1,
            3: 1,
            4: 1
            }
        
    elif angulo == 380:
        switch={
            1: -1,
            2: -1,
            3: -1,
            4: -1
            }
        
    return (switch.get(M,1))

    
