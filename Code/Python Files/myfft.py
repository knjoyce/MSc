import numpy as np

def myfft(time,data):
    
    n=np.size(time)
    dt=(time[2]-time[1])*1e6
    f=np.fft.fftshift(np.fft.fftfreq(n,d=dt))*1000
    FT=np.fft.fftshift(np.fft.fft(data - np.mean(data)))
    
    return f,FT