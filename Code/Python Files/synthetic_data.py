import numpy as np

def synthetic_data(f,n,ppc,Tmax):

    # Input Variables:
    # f = frequency, Hz
    # n = number of cycles, int
    # ppc = points per cycle, int
    # Tmax = max time, s

    w = 2*np.pi*f # angular frequency, Hz
    T = 1/f       # period, s
    
    wave_stop = n*T    # calculates time range for n cycles

    dt = T/ppc   # timestep needed to maintain ppc
    Time = np.arange(0,Tmax,dt) # zero vector of total time (start,stop,step)
    wave_time = np.arange(0,wave_stop,dt)
    y = np.sin(2*np.pi*f*wave_time) # generate synthetic waves
    pad = len(Time) - len(y) 
    y = np.pad(y, (0,pad)) # add zeros to y such that len(y) = len(time) to maintain total time

    #time = time/1e6 # change time back to us
    
    return y,Time

