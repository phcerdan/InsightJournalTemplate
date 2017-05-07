import numpy as np
import matplotlib.pyplot as plt
plt.style.use('grayscale')
plt.tight_layout()
# t = np.linspace(np.pi, 10*np.pi,num=400, endpoint=False)
t = np.linspace(0, 600,num=600)
# Stationary harmonic function: mono-frequency
fLow = np.sin(6*t*np.pi/600.0)
fHigh = np.sin(30*t*np.pi/600.0)
fLH = fLow + fHigh
pf, pa = plt.subplots(2, 2, sharex=True)

# pa[0, 0].plot(t,fLow)
# pa[0, 0].set_xlabel('t')
# pa[0, 0].set_title('fLow')
# pa[1, 0].plot(t,fHigh)
# pa[1, 0].set_xlabel('t')
# pa[1, 0].set_title('fHigh')
pa[0, 0].plot(t,fLH.real)
# pa[0, 0].set_xlabel('t')
pa[0, 0].set_title('Time Domain')
pa[0, 0].set_ylabel('$S_{low} + S_{high}$')

freq = np.fft.fftfreq(t.shape[-1])
fftLH = np.fft.fft(fLH)
fftLHMagn = np.abs(fftLH)
pa[0, 1].plot(t,fftLHMagn)
pa[0, 1].set_title('Frequency Domain')

# Create a non-stationary function.
fNs = np.sin(3*t*np.pi/600.0)
fNs[0:300] = fLow[0:300] #np.sin(3*t[0:300]*np.pi/600.0)
fNs[300:600] = fHigh[300:600] #np.sin(30*t[300:600]*np.pi/600.0)

# pa[0, 0].plot(t,fNs)
# pa[0, 0].set_title('sin(3t)')
# pa[0, 1].plot(t,fNs)
# pa[0, 1].set_title('fHigh=0.5*sin(30t)')
pa[1, 0].plot(t,fNs)
pa[1, 0].set_xlabel('$t$')
pa[1, 0].set_ylabel('Non-stationary $S_{ns}$')

fftNs= np.fft.fft(fNs)
fftNsMagn = np.abs(fftNs)
pa[1, 1].plot(t,fftNsMagn)
pa[1, 1].set_xlabel('$f$')

# Fine-tune figure; make subplots close to each other and hide x ticks for
# all but bottom plot.
pf.subplots_adjust(hspace=0.1)
plt.setp(pf.axes[0].get_xticklabels(), visible=False)
plt.setp(pf.axes[1].get_xticklabels(), visible=False)
# plt.setp([a.get_xticklabels() for a in pf.axes[:-1]], visible=False)

# pf.set_figheight(9.6)
# pf.set_figwidth(12.8)
# pf.savefig('spatial_localization_fft.pdf', bbox_inches='tight')
# pf.savefig('spatial_localization_fft.svg', format='svg', bbox_inches='tight')
pf.show()
