#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import os,sys
import itertools
import matplotlib as mpl
def run(file_in):
    colors_array = mpl.colors.cnames.keys()
    colors_array = ['black']
    colorStyles = itertools.cycle(colors_array)
    markers_array = mpl.markers.MarkerStyle.markers.keys()
    lines_array = mpl.lines.lineStyles.keys()
    lines_array = ['-', '--', ':', '-.']
    lineStyles = itertools.cycle(lines_array)
    markers_array = ['None',',', '+', '.', 'o', '*']
    markerStyles = itertools.cycle(markers_array)

    data = np.loadtxt(file_in, delimiter=',')
    bands = data[0,:].size - 1;
    w = data[:,0]
    fig, ax = plt.subplots(1,1)
    for row in range( 1, bands + 1 ):
        if row == 1:
            ax.plot(w,data[:,row],label=str(row - 1) + " LP",
                    linestyle = next(lineStyles),
                    # marker = next(markerStyles), markevery=0.5,
                    color = next(colorStyles));
        elif row == bands:
            ax.plot(w,data[:,row], label=str(row - 1) + " HP",
                    linestyle = next(lineStyles),
                    # marker = next(markerStyles), markevery=0.5,
                    color  = next(colorStyles));
        else:
            ax.plot(w,data[:,row], label=str(row - 1),
                    linestyle = next(lineStyles),
                    # marker = next(markerStyles), markevery=0.5,
                    color  = next(colorStyles));

    # plt.tick_params(
    #     axis='x',which='both',      # both major and minor ticks are affected
    #     bottom='off',top='off')
    # ax.set_xticks(np.arange(0.0, 0.5 + 0.1, 1.0/32.0))
    # labels = [item.get_text() for item in ax.get_xticklabels()]
    # labels[0] = '0';
    # labels[8] = '$\pi/2$';
    # labels[16] = '$\pi$';
    # ax.set_xticklabels(labels)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend(loc="best", title="SubBand $i$:")
    ax.set_ylim(-0.0,1.01);
    ax.set_yticks(np.arange(0.0, 1.0 + 0.1, 1.0))
    ax.set_ylabel('$\hat{h_i}(\omega)$', rotation='horizontal', va='top')
    ax.set_xlim(0,0.52); # w_max = N/2 / N = 0.5
    ax.set_xticks([0.0, 0.25, 0.5])
    ax.set_xticklabels(['0', '$\pi/2$', '$\pi$'])
    ax.set_xlabel('$\omega$ [rad/s]')
    file_base = os.path.splitext(str(file_in))[0] #/path/to/filename, without .txt
    file_out = file_base + ".png"
    fig.savefig(file_out, bbox_inches='tight');
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.show()
    plt.clf()
    plt.cla()
    plt.close()
    # plt.close(fig)
    # fig.show()

if __name__ == '__main__':
    file_in = sys.argv[1];
    run(file_in)
