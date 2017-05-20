import numpy as np
import matplotlib.pyplot as plt
import os,sys
import itertools
import matplotlib as mpl
def run(file_bands):
    colors_array = mpl.colors.cnames.keys()
    colors_array = ['black']
    colorStyles = itertools.cycle(colors_array)
    markers_array = mpl.markers.MarkerStyle.markers.keys()
    lines_array = mpl.lines.lineStyles.keys()
    lines_array = ['-', '--', ':', '-.']
    lineStyles = itertools.cycle(lines_array)
    markers_array = ['None',',', '+', '.', 'o', '*']
    markerStyles = itertools.cycle(markers_array)

    data_bands = np.loadtxt(file_bands, delimiter=',')
    bands = data_bands[0,:].size - 1;
    w = data_bands[:,0]
    fig_bands, ax_bands = plt.subplots(1,1)
    for row in range( 1, bands + 1 ):
        if row == 1:
            ax_bands.plot(w,data_bands[:,row],label=str(row - 1) + " LP",
                    linestyle = next(lineStyles),
                    # marker = next(markerStyles), markevery=0.5,
                    color = next(colorStyles));
        elif row == bands:
            ax_bands.plot(w,data_bands[:,row], label=str(row - 1) + " HP",
                    linestyle = next(lineStyles),
                    # marker = next(markerStyles), markevery=0.5,
                    color  = next(colorStyles));
        else:
            ax_bands.plot(w,data_bands[:,row], label=str(row - 1),
                    linestyle = next(lineStyles),
                    # marker = next(markerStyles), markevery=0.5,
                    color  = next(colorStyles));

            ax_bands.legend(loc="best", title="SubBand:")
    ax_bands.set_ylabel(str(bands) + ' Subbands')
    ax_bands.set_ylim(-0.1,1.1);
    ax_bands.set_xlim(0,0.52); # w_max = N/2 / N = 0.5
    ax_bands.set_xlabel('w [Hz]')
    file_bands_base = os.path.splitext(str(file_bands))[0] #/path/to/filename, without .txt
    file_bands_out = file_bands_base + ".png"
    fig_bands.savefig(file_bands_out);
    plt.show()
    # fig_bands.show()

if __name__ == '__main__':
    file_bands = sys.argv[1];
    run(file_bands)
