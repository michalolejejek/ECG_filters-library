import ECG_filters as ef
import numpy as np
import matplotlib.pyplot as plt


ecg = np.loadtxt('data.csv', skiprows=0)

sample_freq = 1000
high_ctf = 0.5
low_ctf = 2
line_power = 60
order = 5

plt.figure(1)
x1 = plt.subplot(211)
plt.plot(ecg)
x1.set_title("Raw ECG signal")

filtered_signal = ef.filter_all(ecg, sample_freq, order)
x2 = plt.subplot(212)
plt.plot(filtered_signal)
x2.set_title("Clean ECG signal")
plt.show()