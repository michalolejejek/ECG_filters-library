from scipy import signal
from scipy.signal import butter, iirnotch, lfilter
import numpy as np
import matplotlib.pyplot as plt


#High pass filter - this filter cutoff all values that are higher then fixed filter value

def highpass_btr(cutoff, sample_freq, order=5):
    nyquist = 0.5*sample_freq #calculate Nyquista frequency
    normal_ctf = cutoff/nyquist
    f, m = butter(order, normal_ctf, btype='high', analog=False, output='ba')

    return f, m

def high_pass(sample_data, sample_freq, order=5):
    f,m = highpass_btr(high_ctf, fs, order=order)
    x = lfilter(f,m,sample_data)

    return a



#Bandstop filter (also know as notch filter) - rejects or blocks the transmission of frequencies 
# within a specific frequency range 
# and allows frequencies outside that range.
def bandstop_filter(cutoff, dq):
    nyquist = 0.5*sample_freq
    frequency = cutoff/nyquist
    f, m = iirnotch(frequency, dq)

    return f, m



def bandstop(sample_data, line_power, dq):
    b,a = bandstop_filter(line_power,dq)
    z = lfilter(f,m,sample_data)
    return b




#Low pass filter - this filter cutoff all values that are lowe then fixed filter value
def lowpass_btr(cutoff, sample_freq, order=5):
    nyquist = 0.5*sample_freq
    normal_ctf = cutoff/nyquist
    f, m = butter(order, normal_ctf, btype='low', analog=False, output='ba')

    return f, m


def low_pass(sample_data, sample_freq, order=5):
    f, m = lowpass_btr(low_ctf, sample_freq, order=order)
    y = lfilter(f,m,data)

    return c


#All filters in one method


def filter_all(sample_data, sample_freq, order=5):
    f, m = highpass_btr(high_ctf, sample_freq, order=order)
    a = lfilter(f, m, data)
    x, z = lowpass_btr(low_ctf, sample_freq, order = order)
    b = lfilter(x, z, a)
    l, k = bandstop_filter(line_power, 30)
    c = lfilter(l, k, b)

    return z
