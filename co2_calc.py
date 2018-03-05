import sys
import os.path
import argparse
import numpy as np
from transport import Transport
import utils

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('households', nargs='?', type=int, default=5, help='number of households (default: %(default)s)')
parser.add_argument('--input', '-i', default='/input', help='input folder (default: %(default)s)')
parser.add_argument('--output', '-o', default='/output', help='output folder (default: %(default)s)')
args = parser.parse_args()

def km_to_world(km):
    return km / 40000

co2_kg = args.households * 3000
transport = Transport(co2_kg)

# 1. Print traveling kilometers per transport type.
print("For {} households, Nerdalize reduces CO2 emissions by {:,d} kg per year.".format(args.households, co2_kg))
print("")
print("This is equivalent to (per person):")
tmpl = "- {:,.0f} Kilometers by {}, or {:.1f} times around the world! {}"
print(tmpl.format(transport.car(), "car", km_to_world(transport.car()), "🚗"))
print(tmpl.format(transport.train(), "train", km_to_world(transport.train()), "🚆"))
print(tmpl.format(transport.airplane(), "airplane", km_to_world(transport.airplane()), "✈️ "))

# define input and output files
input_file = args.input + "/flights.csv"
output_file = args.output + '/flights.png'

# 2. Read input file and plot amount of trips that could be made for amount of households.
if os.path.isfile(input_file):
    try:
        utils.mkdir(args.output)
        x = []
        y = []
        flights = np.genfromtxt(input_file, delimiter=',', names=True, dtype=None, encoding='utf-8')
        for flight in flights:
            x.append(flight['flight'])
            y.append(transport.airplane() / float(flight['distance']))

        utils.plot(x, y,
            'Flights',
            'Number of trips',
            'The amount of trips you can make by ✈️ per year, for {} households.'.format(args.households),
            output_file)

        print("\n>> Created flights plot {}".format(output_file))
    except OSError as e:
        _, strerror = e.args
        print("Failed to create output folder {}: {}".format(args.output, strerror))
        sys.exit(1)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        sys.exit(2)
