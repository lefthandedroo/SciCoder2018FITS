import argparse

from spectrum import Spectrum

parser = argparse.ArgumentParser(description="Plot spectra of given file",
										usage="spectrum.py --filepath datafile.fits")

parser.add_argument("-f", "--filepath", help="the data file to be read")

args = parser.parse_args()

figure = Spectrum(args.filepath)
figure.plot("Name")
