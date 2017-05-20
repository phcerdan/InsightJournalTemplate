#!/env/python
import itertools
import motherWaveletFrequencyTiling
import waveletSubBands
import os,sys
file_root = sys.argv[1];
bands = str(sys.argv[2]);
# file_root = '/home/phc/Software/ITK/build/Testing/Temporary/profileMotherWavelet'
# bands = str(2);
wavelets = ['_Held_', '_Simoncelli_', '_Vow_', '_Shannon_']
terminations = ['_Mother.txt', '_SubBands.txt']
files = [file_root + w + bands + t for w in wavelets for t in terminations]
files_mother = [file_root + w + bands + terminations[0] for w in wavelets]
files_bands = [file_root + w + bands + terminations[1] for w in wavelets]

for f in files_mother:
    waveletSubBands.run(f);
for f in files_bands:
    motherWaveletFrequencyTiling.run(f);
