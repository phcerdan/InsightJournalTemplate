import itk
import numpy as np
import matplotlib.pyplot as plt
# import numpy.fft as fft
np.core.arrayprint._line_width = 200

Dimension = 2
RealPixelType = itk.F
RealImageType = itk.Image[RealPixelType, Dimension]

# Read input Image
inputImage = "/home/phc/Software/ITK/build-dev-cpp98/ExternalData/Modules/Remote/IsotropicWavelets/test/Input/checkershadow_Lch_512x512.tiff"
reader = itk.ImageFileReader.New(FileName=inputImage)
spacing = reader.GetOutput().GetSpacing()
origin = reader.GetOutput().GetOrigin()
direction = reader.GetOutput().GetDirection()

# Perform FFT on input image
castFilter = itk.CastImageFilter[itk.output(reader), RealImageType].New(reader)
fftFilter = itk.ForwardFFTImageFilter.New(castFilter)
fftFilter.Update()
ComplexType=itk.output(fftFilter.GetOutput())
npInput = itk.GetArrayFromImage(castFilter)
npFFT = itk.GetArrayFromImage(fftFilter)
plt.imshow(npInput)
itk.show(reader)
# plt.show()

inputImage3D = "/home/phc/Software/ITK/build-dev-cpp98/ExternalData/Modules/Remote/IsotropicWavelets/test/Input/collagen_21x21x9.tiff"
reader3D = itk.ImageFileReader.New(FileName=inputImage)
npInput3D = itk.GetArrayFromImage(reader3D)
