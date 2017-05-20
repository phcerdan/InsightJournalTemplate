import numpy as np
import matplotlib.pyplot as plt
import os,sys
import itertools
import matplotlib as mpl
def run(file_mother):
    colors_array = mpl.colors.cnames.keys()
    colors_array = ['black']
    colorStyles = itertools.cycle(colors_array)
    markers_array = mpl.markers.MarkerStyle.markers.keys()
    lines_array = mpl.lines.lineStyles.keys()
    lines_array = ['-', '--', ':', '-.']
    lineStyles = itertools.cycle(lines_array)
    markers_array = ['None',',', '+', '.', 'o', '*']
    markerStyles = itertools.cycle(markers_array)

    # file_mother = '/home/phc/Software/ITK/build/Testing/Temporary/profileMotherWavelet_Held_1_Mother.txt
    file_mother_base = os.path.splitext(str(file_mother))[0] #/path/to/filename, without .txt
    file_mother_out = file_mother_base + ".png"
    fig_mother, ax_mother = plt.subplots(1,1)
    data_mother = np.loadtxt(file_mother, delimiter=',')
    levels = data_mother[0,:].size - 1;
    w = data_mother[:,0]
    for row in range( 1, levels + 1 ):
        ax_mother.plot(w,data_mother[:, row], label = str(row-1),
                    linestyle = next(lineStyles),
                    # marker = next(markerStyles), markevery=0.,
                    color = next(colorStyles));

    ax_mother.legend(loc="best", title="Levels:")
    ax_mother.set_xlim(0,0.52); # w_max = N/2 / N = 0.5
    ax_mother.set_ylabel('Mother Wavelet')
    ax_mother.set_ylim(-0.1,1.1);
    ax_mother.tick_params(labeltop='on')
    fig_mother.savefig(file_mother_out);
    plt.show()
    # fig_mother.show()

if __name__ == '__main__':
    file_mother = sys.argv[1];
    run(file_mother)
