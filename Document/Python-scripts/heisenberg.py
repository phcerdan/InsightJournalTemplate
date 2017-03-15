import numpy as np
import matplotlib.pyplot as plt
# t = np.linspace(np.pi, 10*np.pi,num=400, endpoint=False)
t = np.linspace(0, 200,num=200)
# Stationary harmonic function: mono-frequency
f = np.sin(2*np.pi*5*t)
# Create a non-stationary function.
f2 = np.sin(2*np.pi*15*t)
f2[0:50] = np.sin(2*np.pi*5*t[0:50])
f2[50:100] = np.sin(2*np.pi*10*t[0:50])
f2[100:150] = np.sin(2*np.pi*15*t[0:50])
f2[150:200] = np.sin(2*np.pi*20*t[0:50])
fsum = f + f2
pf, pa = plt.subplots(2, 3)
# pa[0, 0].plot(t,f)
pa[0, 0].plot(t,f2)
pa[0, 0].set_ylabel('t domain')
pa[0, 0].set_title('f1=sin(t), f2=sin(2pi*t)')
pa[0, 1].plot(t,fsum)
pa[0, 1].set_title('fsum=f1+f2')

freq = np.fft.fftfreq(t.shape[-1])
ft = np.fft.fft(f)
ft2 = np.fft.fft(f2)
ftsum = np.fft.fft(fsum)
# f[int(t.size*1/4):] = 0
# f2[0:int(t.size*3/4)] = 0
f_segment = f + f2
pa[0, 2].plot(t,f_segment)
pa[0, 2].set_title('f1 + A*f2')
ft_segment = np.fft.fft(f_segment)

pa[1, 0].plot(freq,ft.real,freq,ft.imag)
pa[1, 0].plot(freq,ft2.real, freq, ft2.imag)
pa[1, 0].set_ylabel('fft, dual space')
pa[1, 1].plot(freq,ftsum.real, freq,ftsum.imag)
pa[1, 2].plot(freq,ft_segment.real, freq, ft_segment.imag)
# pf.set_figheight(40)
# pf.set_figwidth(40)
pf.savefig('spatial_localization_fft.pdf', bbox_inches='tight')
plt.show()
