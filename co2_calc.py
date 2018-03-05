import sys
import os.path
import numpy as np
from transport import Transport
import utils

households = 5 if len(sys.argv) < 2 else int(sys.argv[1])
output_folder = '/output' if len(sys.argv) < 3 else sys.argv[2]
input_folder = '/input' if len(sys.argv) < 4 else sys.argv[3]

def km_to_world(km):
    return km / 40000

co2_kg = households * 3000
transport = Transport(co2_kg)

# 1. Print traveling kilometers per transport type.
print("For {} households, Nerdalize reduces CO2 emissions by {:,d} kg per year.".format(households, co2_kg))
print("")
print("This is equivalent to (per person):")
tmpl = "{} {:,.0f} Kilometers by {}, or {:.1f} times around the world 🌍"
print(tmpl.format("🚗", transport.car(), "car", km_to_world(transport.car())))
print(tmpl.format("🚆", transport.train(), "train", km_to_world(transport.train())))
print(tmpl.format("✈️ ", transport.airplane(), "airplane", km_to_world(transport.airplane())))

# 2. Read input file and plot amount of trips that could be made for amount of households.
input_file = input_folder + "/flights.csv"
if os.path.isfile(input_file):
    try:
        utils.mkdir(output_folder)
        output_file = output_folder + '/flights.png'

        x = []
        y = []
        flights = np.genfromtxt(input_file, delimiter=';', names=True, dtype=None, encoding='utf-8')
        for flight in flights:
            x.append(flight['flight'])
            y.append(transport.airplane() / float(flight['distance']))

        utils.plot(x, y,
            'Flights',
            'Number of trips',
            'The amount of trips you can make by ✈️ per year, for {} households.'.format(households),
            output_file)

        print("\n>> Created flights plot {}".format(output_file))
    except OSError as e:
        _, strerror = e.args
        print("Failed to create output folder {}: {}".format(output_folder, strerror))
        sys.exit(1)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        sys.exit(2)
