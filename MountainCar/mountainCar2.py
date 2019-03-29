import numpy as np

def next_state(v, p, a, pos, vel):

    v_cont = v + 0.001 * a - 0.0025 * np.cos(3 * p)
    p_cont = p + v

    min_val_v = abs(v_d - vel[0])
    v_d = vel[0]
    min_val_p = abs(p_d - pos[0])
    p_d = pos[0]

    for i in range(len(vel)):
        val_v = abs(v_cont - vel[i])
        val_p = abs(p_cont - pos[i])

        if val_v < min_val_v:
            min_val_v = val_v
            v_d = vel[i]
        if val_p < min_val_p:
            min_val_p = val_p
            p_d = pos[i]


    return v_d, p_d

def reward(v_d, p_d, pos): # the values for current state and action are encoded in the next state (deterministic)

    if p_d == pos[len(pos)-1]:
        return 1000
    
    if p_d == pos[0]:
        return -1000

    return 0

#def BellmanOp(V, vel, pos):



def main():

    vel = np.linspace(-0.07, 0.07, 101)
    pos = np.linspace(-1.2, 0.5, 101)
    

if __name__ == '__main__':
    main()    