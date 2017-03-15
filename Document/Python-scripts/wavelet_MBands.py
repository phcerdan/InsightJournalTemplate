import numpy as np
import matplotlib.pyplot as plt
import os,sys
try:
    plt.style.use('ggplot')
except:
    pass
file_in = sys.argv[1];
print (file_in)
fig, (ax1,ax2) = plt.subplots(2,1, sharex=True)
data = np.loadtxt(file_in, delimiter=',')
bands = data[0,:].size - 2;
w = data[:,0]
for row in range( 1,bands + 1 ):
    if row == 1:
        ax2.plot(w,data[:,row], label=str(row - 1) + " LP");
    elif row == bands:
        ax2.plot(w,data[:,row], label=str(row - 1) + " HP");
    else:
        ax2.plot(w,data[:,row], label=str(row - 1));
    ax2.legend(loc="best")
ax2.set_ylabel(str(bands) + ' subbands')
ax2.set_ylim(-0.1,1.1);
ax1.plot(w,data[:, bands+1])
ax1.set_ylabel('Mother Wavelet')
ax1.set_ylim(-0.1,1.1);
ax1.tick_params(labeltop='on')
ax2.set_xlim(0,0.52); # w_max = N/2 / N = 0.5
plt.xlabel('w [Hz]')
plt.tight_layout()
fig.subplots_adjust(hspace=0)
file_base = os.path.splitext(str(file_in))[0];
file_out = file_base + ".png";
fig.savefig(file_out);
plt.show()
