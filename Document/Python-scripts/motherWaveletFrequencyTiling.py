#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import os,sys
import itertools
import matplotlib as mpl
def run(file_in):
    # plt.rc('text', usetex=True)
    colors_array = mpl.colors.cnames.keys()
    colors_array = ['black']
    colorStyles = itertools.cycle(colors_array)
    markers_array = mpl.markers.MarkerStyle.markers.keys()
    lines_array = mpl.lines.lineStyles.keys()
    lines_array = ['-', '--', ':', '-.']
    lineStyles = itertools.cycle(lines_array)
    markers_array = ['None',',', '+', '.', 'o', '*']
    markerStyles = itertools.cycle(markers_array)

    # file_in = '/home/phc/Software/ITK/build/Testing/Temporary/profileMotherWavelet_Held_1_Mother.txt'
    file_base = os.path.splitext(str(file_in))[0] #/path/to/filename, without .txt
    file_out = file_base + ".png"
    fig, ax = plt.subplots(1,1)
    data = np.loadtxt(file_in, delimiter=',')
    levels = data[0,:].size - 1;
    w = data[:,0]
    for row in range( 1, levels + 1 ):
        ax.plot(w,data[:, row], label = str(row-1),
                    linestyle = next(lineStyles),
                    # marker = next(markerStyles), markevery=0.,
                    color = next(colorStyles));

    plt.tick_params(
        axis='x',which='both',      # both major and minor ticks are affected
        bottom='off',top='off')
    ax.set_yticks(np.arange(0.0, 1.0 + 0.1, 1.0))
    ax.set_xticks(np.arange(0.0, 0.5 + 0.1, 1.0/32.0))
    labels = [item.get_text() for item in ax.get_xticklabels()]
    labels[0] = '0';
    labels[1] = '$\pi/16$';
    labels[2] = '$\pi/8$';
    labels[4] = '$\pi/4$';
    labels[8] = '$\pi/2$';
    labels[16] = '$\pi$';
    ax.set_xticklabels(labels)
    ax.legend(loc="best", title="Level $i$:")
    ax.set_xlim(0,0.501); # w_max = N/2 / N = 0.5
    ax.set_xlabel('$\omega$ [rad/s]')
    ax.set_ylabel('$\hat{\psi}(2^{i}\omega)$', rotation='horizontal', va='top')
    ax.set_ylim(-0.0,1.01);
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    fig.savefig(file_out);
    plt.show()
    plt.clf()
    plt.cla()
    plt.close()
    # plt.close(fig)

if __name__ == '__main__':
    file_in= sys.argv[1];
    run(file_in)
